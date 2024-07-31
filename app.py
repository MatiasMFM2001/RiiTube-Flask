#!/usr/bin/env python3

from flask import Flask
import os

app = Flask(__name__)

app.config["SECRET_KEY"] = os.urandom(32).hex()
app.config["SERVER_NAME"] = None

app.config["YT_DLP_CONFIG"] = {
    "outtmpl": "-",
    "logtostderr": True,
    #"format": "[width <= 640]",
    "format": "best [height <= 480]",
}

with app.app_context():
    import youtube

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)

