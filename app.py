import os
import pickle
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# --- Example 1: Command Injection ---
@app.route("/run")
def run_command():
    # BAD: User input is passed directly into an OS command
    cmd = request.args.get("cmd")
    os.system(f"echo Running command: {cmd}")  # CodeQL will flag this

    return f"Executed: {cmd}"

# --- Example 2: SQL Injection ---
@app.route("/user")
def get_user():
    user_id = request.args.get("id")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # BAD: Query built with unsanitized user input
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)  # CodeQL should detect SQL injection here

    result = cursor.fetchall()
    conn.close()
    return str(result)

# --- Example 3: Insecure Deserialization ---
@app.route("/load")
def load_data():
    data = request.args.get("data")
    # BAD: Using pickle.loads on untrusted input
    obj = pickle.loads(bytes(data, "utf-8"))  # CodeQL will flag this
    return str(obj)

@app.route("/")
def home():
    return "CodeQL Demo App Running!"

if __name__ == "__main__":
    app.run(debug=True)
