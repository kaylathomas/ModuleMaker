# main.py
import click
import json
import subprocess

# Dependencies
import FilesNFolders
from RailsStringMethods import underscore

# File contents
from .new.module_structure import module_layout

@click.command()
@click.argument('module_name')
@click.argument('submodules', nargs=-1)
@click.option('--click', is_flag=True, help="Include click import in the core module file.")
@click.option('--init', is_flag=True, help="Initialize the module as a Git repository.")
def new_command(module_name, submodules, click, init):
    folders, files, file_contents = build_module(module_name, submodules, use_click=click)
    update_gitignore_and_module_info(module_name, files, file_contents)

    if init:
        initialize_git_repository(module_name)

def build_module(module_name, submodules, use_click=False):
    # Generate the structure of the module
    structure = module_layout(module_name)

    generate_template(
        structure["folders"],
        structure["files"],
        structure["file_contents"],
    )

    # Define initial content for module_info.json
    module_info_content = {
        "module_name": module_name,
        "version_number_0": 0,
        "version_number_1": 0,
        "version_number_2": 1,
        "required_modules": [],
        "packages": [underscore(submodule) for submodule in submodules]
    }

    # Generate module_info.json file
    file_contents[f"{module_name}/module_info.json"] = [json.dumps(module_info_content, indent=4)]

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
