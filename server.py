from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'public'), filename)

if __name__ == '__main__':
    app.run(debug=True)
