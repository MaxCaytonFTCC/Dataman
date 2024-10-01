# Minimal Flask App
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    

    # Or Redirect to itself during POST (or other)
    return redirect(url_for('operand1'))

@app.route("/operand1")
def operand1():
    
    # Either show the page...
    if request.method == "GET":
        return render_template("operand1.html")

    # Or Redirect to itself during POST (or other)
    return redirect(url_for('index'))

@app.route("/operation")
def operation():
    
    # Either show the page...
    if request.method == "GET":
        return render_template("operation.html")

    # Or Redirect to itself during POST (or other)
    return redirect(url_for('index'))

@app.route("/operand2")
def operand2():
    
    # Either show the page...
    if request.method == "GET":
        return render_template("operand2.html")

    # Or Redirect to itself during POST (or other)
    return redirect(url_for('index'))