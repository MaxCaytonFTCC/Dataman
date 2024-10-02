# Minimal Flask App
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    # Or Redirect to itself during POST (or other)
    return redirect(url_for('operand1'))

@app.route("/operand1", methods=["GET", "POST"])
def operand1():
    
    if (request.method == "POST"):
        currentEquation = request.form['display']
        print(f"Received value: {currentEquation}")
        
        return render_template('operand1.html', operand1=currentEquation)
    return render_template('operand1.html', operand1='')
    

    # Redirect to Operand2
    return redirect(url_for('index'))

@app.route("/operation", methods=["GET", "POST"])
def operation():
    
    # Either show the page...
    if request.method == "GET":
        return render_template("operation.html")

    # Or Redirect to itself during POST (or other)
    return redirect(url_for('index'))

@app.route("/operand2", methods=["GET", "POST"])
def operand2():
    
    # Either show the page...
    if request.method == "GET":
        return render_template("operand2.html")

    # Or Redirect to itself during POST (or other)
    return redirect(url_for('index'))