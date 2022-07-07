from flask_cors import cross_origin

from app import app


@app.route('/', methods=['POST'])
@cross_origin()
def main():
    return 1234
