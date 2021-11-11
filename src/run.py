from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__,
            static_folder=None)

cors = CORS(app,
            resources={ r'/api/*' : { 'origins' : '*' } })

@app.route('/', defaults={ 'path': 'index.html' })
@app.route('/<path:path>')
def catch_all(path):
    return send_from_directory('./client/dist', path)
