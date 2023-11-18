# main.py
import click
import json
import subprocess
from FilesNFolders import generate_template, generate_files, generate_file_contents
from RailsStringMethods import underscore

@click.command()
@click.argument('module_name')
@click.argument('submodules', nargs=-1)
@click.option('--click', is_flag=True, help="Include click import in the core module file.")
@click.option('--init', is_flag=True, help="Initialize the module as a Git repository.")
def new_command(module_name, submodules, click, init):
    folders, files, file_contents = build_module(module_name, submodules, use_click=click)
    update_gitignore_and_module_info(module_name, files, file_contents)

    generate_template(folders=folders, files=files, file_contents=file_contents)

    if init:
        initialize_git_repository(module_name)

def build_module(module_name, submodules, use_click=False):
    core_file_name = f"{underscore(module_name)}_core.py"
    folders = [module_name]
    files = [
        f"{module_name}/setup.py",
        f"{module_name}/setup.cfg",
        f"{module_name}/README.md",
        f"{module_name}/.gitignore",
        f"{module_name}/__init__.py",
        f"{module_name}/{core_file_name}",
        f"{module_name}/module_info.json"
    ]

    file_contents = {
        f"{module_name}/setup.py": setup_py_contents(module_name),
        f"{module_name}/setup.cfg": ["[metadata]\ndescription-file = README.md\n"],
        f"{module_name}/{core_file_name}": core_file_contents(use_click),
        # ... other default contents ...
    }

    # Define initial content for module_info.json
    module_info_content = {
        "module_name": module_name,
        "version": "0.1",
        "required_modules": [],
        "packages": [underscore(submodule) for submodule in submodules]
    }

    file_contents[f"{module_name}/module_info.json"] = [json.dumps(module_info_content, indent=4)]

    for submodule in submodules:
        submodule_folder = f"{module_name}/{underscore(submodule)}"
        submodule_file = f"{submodule_folder}/main.py"
        folders.append(submodule_folder)
        files.append(submodule_file)
        file_contents[submodule_file] = ["# main.py\n"]

    return folders, files, file_contents

def update_gitignore_and_module_info(module_name, files, file_contents):
    gitignore_path = f"{module_name}/.gitignore"
    gitignore_content = "\n".join(["# .gitignore file", "module_info.json"])
    file_contents[gitignore_path] = [gitignore_content]

def core_file_contents(use_click):
    lines = ["# Core module file\n"]
    if use_click:
        lines.insert(0, "import click\n")
    return lines

def setup_py_contents(module_name):
    return [
        "from distutils.core import setup\n\n",
        "setup(\n",
        f"  name='{module_name}',\n",
        f"  packages=['{module_name}'],\n",
        "  version = '0.1',\n",
        # ... other setup.py contents ...
    ]

def initialize_git_repository(module_name):
    try:
        subprocess.run(["git", "init", module_name], check=True)
        print(f"Initialized a new Git repository in {module_name}/")
    except subprocess.CalledProcessError as e:
        print(f"Failed to initialize Git repository: {e}")
