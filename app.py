from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert")
def convert():
    amount = request.args.get("amount", type=float)
    from_currency = request.args.get("from")
    to_currency = request.args.get("to")

    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    response = requests.get(url)
    data = response.json()

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)