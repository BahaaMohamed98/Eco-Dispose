import os

# base directory of the server
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# relative path for upload folder
UPLOAD_FOLDER = "static/uploads"

# absolute path for file saving
UPLOAD_FOLDER_PATH = os.path.join(BASE_DIR, UPLOAD_FOLDER)

# allowed file upload extensions
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
