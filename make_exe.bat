::pyinstaller --onefile --add-data "templates;templates" --add-data "instance;instance" app.py --hidden-import flask_bcrypt
pyinstaller --onefile splitter.py