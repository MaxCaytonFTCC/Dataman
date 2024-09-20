# Minimal Flask App
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config["DEBUG"] = True
# TODO Make this a database
comments = []

@app.route("/", methods=["GET", "POST"])
def index():
    
    # Either show the page...
    if request.method == "GET":
        return render_template("main_page.html", comments=comments)

    # Or add a comment then redirect to the page
    comments.append(request.form["contents"])
    return redirect(url_for('index'))
