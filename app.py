from datetime import datetime
from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/time")
def server_time():
    return jsonify(time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
