import json
from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)

SERVER_IP = "192.168.0.100"
SERVER_PORT = 5000
UPLOADS_PATH = "static/uploads"

latest_data = {
    "description": "Oczekiwanie na polaczenie z samolotem...",
    "filename": "",
    "date": ""
}

try:
    with open("data/last_image.json", "r") as f:
        latest_data = json.loads(f.read())
except FileNotFoundError:
    os.mkdir("data")
    with open('data/last_image.json', 'w') as f:
        f.write('{"description": "Oczekiwanie na polaczenie z samolotem...","filename": "","date": ""}')

if not os.path.exists(UPLOADS_PATH):
    os.mkdir(UPLOADS_PATH)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/post_image", methods=["POST"])
def post_image():
    if 'image' not in request.files:
        return "Nie otrzymano zdjecia", 400

    desc = request.form.get("description")
    image = request.files["image"]
    d = request.form.get("date")
    filename = d.replace(" ", "_").replace(".", "_").replace("-", "_").replace(":", "_")+image.filename

    if image.filename != '':
        filepath = os.path.join(UPLOADS_PATH, filename)
        image.save(filepath)
    else:
        return "Nazwa zdjecia jest pusta", 400

    latest_data['description'] = desc
    latest_data['filename'] = filename
    latest_data["date"] = d

    with open("data/last_image.json", "w") as f:
        json.dump(latest_data, f)

    return "Poprawnie przeslano zdjecie", 200


@app.route("/get_latest", methods=["GET"])
def get_latest():
    return jsonify(latest_data)


if __name__ == "__main__":
    app.run(SERVER_IP, port=SERVER_PORT)
