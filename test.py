import sys
print("INSIDE OF TEST.PY:")
print(sys.path)


from FilesNFolders import generate_template
def render_server_py(flag, settings):
    if flag == "default":
        content = f"""
        #!/usr/bin/env python3
        import sys
        import os

        # Add the parent directory to sys.path to find the 'api' module
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        from api import create_app
        from api.config.init_database import create_database
        from api.db.seeds import generate_seeds
        from api.config.routes import routes
        from flask_cors import CORS

        print("FLASK APP RUNNING")

        # ==========================
        #     APP INITIALIZATION
        # ==========================
        # Initialize the app
        app = create_app()

        CORS(app)
        # Set your static folder
        app.static_folder = '{settings["static_folder_location"]}'

        # Create the database
        create_database(app)
        # Generate seeds
        generate_seeds(app)

        # =================================
        #     ASSET AND DIRECTORY SETUP
        # =================================

        app.register_blueprint(routes)

        if __name__ == '__main__':
            app.run(debug=True, port={settings["port"]}, use_reloader={settings["use_reloader"]})

        """

        return content

def info(app_name):
    return {
        "port": "8000",
        "use_reloader": False,
        "static_folder_location": f"{app_name}/application/static"
    }

"""Create a new Flask application with the given name."""
def default_project_layout(app_name, settings):
    return {
        "folders": {
            f"{app_name}/application",
            f"{app_name}/application/mvc",
            f"{app_name}/application/mvc/models",
            f"{app_name}/application/mvc/views",
            f"{app_name}/application/mvc/controllers",
            f"{app_name}/application/public",
            f"{app_name}/application/test",
            f"{app_name}/application/test/models",
            f"{app_name}/application/test/controllers",
            f"{app_name}/application/bin",
            f"{app_name}/application/db",
            f"{app_name}/application/public",
            f"{app_name}/application/config",
            f"{app_name}/application/scripts",
            f"{app_name}/application/helpers",
            f"{app_name}/application/scripts/javascript",
            f"{app_name}/application/scripts/python",
        },
        "files": {
            f"{app_name}/.gitignore": "",
            f"{app_name}/application/mvc/models/_BaseModel.py": "",
            f"{app_name}/application/scripts/javascript/application.js": "",
            f"{app_name}/application/scripts/python/application.py": "",
            f"{app_name}/application/config/routes.py": "",
            f"{app_name}/application/config/boot.py": "",
            f"{app_name}/application/db/seeds.py": "",
            f"{app_name}/application/server.py": "",
            f"{app_name}/application/requirements.txt": "",
            f"{app_name}/application/config/settings.py": "",
            f"{app_name}/application/public/favicon.ico": "",
            f"{app_name}/application/public/robots.txt": "",
            f"{app_name}/application/filemap.py": "",
        },
        "file_contents": {
            f"{app_name}/application/server.py": render_server_py("default", settings),
        }
    }

test_settings = info("TestApp")
print(f"PORT NAME:", test_settings["port"])

structure = default_project_layout("TestApp", test_settings)

generate_template(
    structure["folders"],
    structure["files"],
    structure["file_contents"],
)