from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = "a1c3fac22f1cd396c37e4b14"   # Replace with a new key

@app.route("/")
def home():

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

    data = requests.get(url).json()

    print(data)      # <-- Add this

    return render_template("index.html", rates=data)

if __name__ == "__main__":
    app.run(debug=True, port=5001)