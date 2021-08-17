import os

from flask import Flask
from datetime import datetime, timedelta, timezone

app = Flask(__name__)

moscow = timezone(timedelta(hours=3))


@app.route("/")
def index():
    """This route sends back to the client the current date and time in Moscow."""
    time = datetime.now(moscow).strftime("%H:%M:%S - %d/%m/%Y")
    return f"<h1>The current time in Moscow is: {time}</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)
