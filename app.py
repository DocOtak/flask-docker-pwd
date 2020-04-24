import os

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    files = []
    for root, dirs, files in os.walk("/context"):
        files = files
        break

    return render_template("index.html", files=files)

@app.route("/analyze/<path:path>")
def analyze(path):
    stats = os.stat(os.path.join("/context", path))

    return render_template("analyze.html", stats=stats, path=path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)