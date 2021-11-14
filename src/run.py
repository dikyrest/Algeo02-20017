from flask import Flask, request, send_from_directory, send_file
from flask_cors import CORS

from compress.compress import compressImage

app = Flask(__name__,
            static_folder=None)

cors = CORS(app,
            resources={ r'/api/*' : { 'origins' : '*' } })

@app.route('/api/compress', methods=['POST'])
def compress_route():
    try:
        file = request.files['file']
        ratio = int(request.form['rate'])
        result = compressImage(file, ratio)
        return send_file(result, mimetype=file.mimetype)
    except:
        return '', 501

@app.route('/', defaults={ 'path': 'index.html' })
@app.route('/<path:path>')
def catch_all(path):
    return send_from_directory('./client/dist', path)
