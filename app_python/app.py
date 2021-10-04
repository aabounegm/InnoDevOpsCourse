import os
import json

from flask import Flask, jsonify
from datetime import datetime, timedelta, timezone

app = Flask(__name__)

moscow = timezone(timedelta(hours=3))

FILE_NAME = "/home/app/data/visits.json"


@app.route("/")
def index():
    """This route sends back to the client the current date and time in Moscow."""
    visits = 0
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            visits = json.load(f)
    else:
        os.makedirs(os.path.dirname(FILE_NAME), exist_ok=True)
    with open(FILE_NAME, "w") as f:
        json.dump(visits + 1, f)
    time = datetime.now(moscow).strftime("%H:%M:%S - %d/%m/%Y")
    return f"<h1>The current time in Moscow is: {time}</h1>"


@app.route("/visits")
def visit():
    """Sends back the total number of visits to the root endpoint."""
    visits = 0
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            visits = json.load(f)
    return jsonify(visits)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)
