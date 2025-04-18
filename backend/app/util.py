import os
import uuid
from werkzeug.utils import secure_filename
from .config import ALLOWED_EXTENSIONS, BASE_DIR, UPLOAD_FOLDER_PATH, UPLOAD_FOLDER


def get_extension(filename):
    return filename.rsplit(".", 1)[1].lower()


def allowed_file(filename):
    return "." in filename and get_extension(filename) in ALLOWED_EXTENSIONS


def save_file(file):
    if file is None or not allowed_file(file.filename):
        return None

    # create upload directory if it doesn't exist
    os.makedirs(UPLOAD_FOLDER_PATH, exist_ok=True)

    extension = get_extension(file.filename)
    unique_name = f"{uuid.uuid4().hex}.{extension}"
    filename = secure_filename(unique_name)

    file_path = "/" + os.path.join(UPLOAD_FOLDER, filename)  # relative file path
    file.save(os.path.join(UPLOAD_FOLDER_PATH, filename))
    return file_path


def delete_file(filename):
    file_path = os.path.join(BASE_DIR, filename[1:])

    if os.path.exists(file_path):
        os.remove(file_path)
