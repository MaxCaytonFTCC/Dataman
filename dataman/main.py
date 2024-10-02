# Minimal Flask App
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    # Or Redirect to itself during POST (or other)
    return redirect(url_for('calculator'))

@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    if (request.method == "POST"):
        currentEquation = request.form['display']
        print(f"Received value: {currentEquation}")
        
        return render_template('calculator.html', currentEquation=currentEquation)
    return render_template('calculator.html', currentEquation='')