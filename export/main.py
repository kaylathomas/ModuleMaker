import click
import os
import pkgutil
import inspect
import importlib
from FilesNFolders import generate_files, generate_file_contents

@click.command()
@click.argument('module_name', required=False)
@click.argument('module_file', required=False)
def export_command(module_name, module_file):
    if module_name == 'all' or not module_name:
        update_all_modules()
    else:
        update_module(module_name, module_file)

def update_all_modules():
    for _, module_name, _ in pkgutil.iter_modules([os.getcwd()]):
        module_path = os.path.join(os.getcwd(), module_name)
        update_module(module_name)
    print("__init__.py files for all modules updated.")

def update_module(module_name, module_file=None):
    module_path = os.path.join(os.getcwd(), module_name)
    if module_file:
        file_path = os.path.join(module_path, f"{module_file}.py")
        functions = get_functions_from_file(file_path)
        update_init_file(module_path, functions, module_file)
    else:
        all_functions = {}
        for _, file_name, _ in pkgutil.iter_modules([module_path]):
            file_path = os.path.join(module_path, f"{file_name}.py")
            functions = get_functions_from_file(file_path)
            all_functions.update(functions)
        update_init_file(module_path, all_functions)

def update_init_file(module_path, functions, module_file=None):
    init_file_path = os.path.join(module_path, '__init__.py')
    existing_lines = []
    if os.path.exists(init_file_path):
        with open(init_file_path, 'r') as file:
            existing_lines = file.readlines()

    new_imports = []
    for func in functions:
        import_statement = f"from .{module_file} import {func}" if module_file else f"from . import {func}"
        if import_statement + '\n' not in existing_lines:
            new_imports.append(import_statement + '\n')

    if new_imports:
        generate_files([init_file_path], logging=False)
        generate_file_contents({init_file_path: new_imports}, logging=False)
        print(f"__init__.py file for {os.path.basename(module_path)} updated.")
    else:
        print(f"__init__.py file for {os.path.basename(module_path)} unchanged.")

def get_functions_from_file(file_path):
    module_name = os.path.splitext(os.path.basename(file_path))[0]
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return [name for name, obj in inspect.getmembers(module) if inspect.isfunction(obj)]
