# .gitignore Setup Report

The .gitignore file is essential for maintaining a clean and secure Git repository by preventing unnecessary or sensitive files from being tracked.

The entries __pycache__/ and *.pyc exclude Python bytecode cache files, which are generated automatically during execution and offer no value in version control.

Directories like venv/ and env/ are ignored because virtual environments contain large binary dependencies that should be recreated locally rather than committed.

Sensitive configuration files such as local_settings.py, .env, and database files like *.sqlite3 or db.sqlite3 are excluded to protect secrets like API keys and prevent conflicts between local and production databases.

Additionally, IDE-specific folders such as .vscode/ and .idea/ are ignored to avoid committing editor settings that vary between developers. 

By filtering out these files, the repository remains lightweight, secure, and focused only on the source code and essential configuration needed for collaboration. This practice ensures that every team member starts with a consistent environment and avoids accidental exposure of private data.