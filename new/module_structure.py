from .folder_contents.setup_py import render_setup_py

def module_layout(module_name, settings):
    return {
        "folders": {},
        "files": {
            f"{module_name}/__init__.py": "",
            f"{module_name}/.gitignore": "",
            f"{module_name}/module_info.json": "",
            f"{module_name}/{module_name.underscore()}_core.py": "",
            f"{module_name}/README.md": "",
            f"{module_name}/setup.cfg": "",
            f"{module_name}/setup.py": ""
        },
        "file_contents": {
            f"setup.py": render_setup_py(module_name),
        }
    }