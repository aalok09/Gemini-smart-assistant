from flask import Flask, render_template, request, jsonify
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.gemini_interface import get_gemini_response

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message")
    response = get_gemini_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
