from flask import Flask
import os

app = Flask(__name__)
PORT = int(os.environ.get("APP_PORT", 4000))

@app.route("/")
def home():
    return "<h1>GH-900 Codespaces Python demo — Hello from Flask!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
