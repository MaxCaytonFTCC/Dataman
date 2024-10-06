# Minimal Flask App
from flask import Flask, render_template, request, redirect, url_for
import answer_checker as answ

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    return redirect(url_for('calculator'))

@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    if (request.method == "POST"):
        currentEquation = request.form['display']
        
        # Check Answer & Place response in Calculator Display
        currentEquation = 'You got it!' if answ.checkAnswer(currentEquation) else 'EEEEEE'
        return render_template('calculator.html', currentEquation=currentEquation)
    
    # GET Response
    return render_template('calculator.html', currentEquation='')

