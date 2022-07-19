import os
import uuid

from flask import make_response, send_file
from werkzeug.utils import secure_filename

from config.common import UPLOAD_FOLDER


class PhotoLoader:
    def __init__(self):
        self._load_url = UPLOAD_FOLDER

    def load(self, data):
        file = data['file']

        if not file:
            return False
        filename = str(uuid.uuid4()) + secure_filename(file.filename)
        file.save(os.path.join(self._load_url, filename))

        return make_response(filename)

    def get(self, photo_name: str):
        return send_file(os.path.join(self._load_url, photo_name))
