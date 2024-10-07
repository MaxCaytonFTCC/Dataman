# Minimal Flask App
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    
    # Either show the page...
    if request.method == "GET":
        return render_template("calculator.html")

    # Or Redirect to itself during POST (or other)
    return redirect(url_for('index'))
