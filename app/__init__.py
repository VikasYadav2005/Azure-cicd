from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Python Azure CI/CD demo!"

@app.route("/add")
def add():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        return jsonify({"result": a + b})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
