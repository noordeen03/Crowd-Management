from flask import Flask, url_for, send_from_directory, send_file
import os

app = Flask(__name__, static_url_path='')

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def hello():
    return "hello!"

@app.route('/predictions')
def get_predictions():
    file_path = os.path.join(BASE_DIR, 'predictions.png')
    return send_file(file_path, mimetype='image/png')

@app.route('/cam')
def get_cam():
    file_path = os.path.join(BASE_DIR, 'cam.png')
    return send_file(file_path, mimetype='image/png')

@app.route('/log')
def get_log():
    file_path = os.path.join(BASE_DIR, 'bar.txt')
    return send_file(file_path)

@app.route('/bar')
def get_bar():
    file_path = os.path.join(BASE_DIR, 'bar.txt')
    return send_file(file_path)

@app.route('/restaurant')
def get_restaurant():
    file_path = os.path.join(BASE_DIR, 'restaurant.txt')
    return send_file(file_path)

if __name__ == "__main__":
    app.run()