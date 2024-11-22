# app.py
from flask import Flask
from flask import request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Kubernetes!"


@app.route("/greet", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}! Welcome to Kubernetes!"
    return '''
        <form method="POST">
            Name: <input type="text" name="name">
            <input type="submit" value="Submit">
        </form>
    '''


@app.route("/info")
def info():
    hostname = os.getenv("HOSTNAME", "Unknown Pod")
    namespace = os.getenv("KUBERNETES_NAMESPACE", "Unknown Namespace")
    return f"""
        <h1>Kubernetes Pod Information</h1>
        <p><b>Pod Name:</b> {hostname}</p>
        <p><b>Namespace:</b> {namespace}</p>
    """


@app.route("/api", methods=["GET"])
def api():
    return {"message": "Hello, Kubernetes!", "status": "success"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
