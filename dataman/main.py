# Minimal Flask App
from flask import Flask, render_template, request, redirect, url_for
import answer_checker as answ
import memory_bank as bank

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    return redirect(url_for('calculator'))

@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    
    # Get Memory Bank Score
    memoryBankScore = request.args.get('memoryBankScore')

    if (request.method == "POST"):
        
        if "bank" in request.form:
            isValid = bank.isValidEquation(request.form['display'])

            outputMessage = 'EEEEEE'
            if (isValid):
                outputMessage = 'Banked!'
                bank.addTolog(request.form['display'])
            return render_template('calculator.html', currentEquation=outputMessage)
        elif "go" in request.form:
            return redirect(url_for('memoryBankGame'))

        currentEquation = request.form['display']
        
        print(currentEquation)

        # Check Answer & Place response in Calculator Display
        currentEquation = 'Correct!' if answ.checkAnswer(currentEquation) else 'EEEEEE'
        return render_template('calculator.html', currentEquation=currentEquation, memoryBankScore=memoryBankScore)
    
    # GET Response
    return render_template('calculator.html', currentEquation='')

@app.route("/memoryBankGame", methods=["GET", "POST"])
def memoryBankGame():
    # Get Next Question
    if (request.method == "POST" and "check" in request.form):
        currentEquation = request.form['display']
        bank.recordAnswer(answ.checkAnswer(currentEquation))

    if (bank.getEquationCount() > 0):
        return render_template('calculator.html', currentEquation=bank.popNextEquation())

    # Display Score
    score = bank.getScore()
    scoreDisplay = "\nCorrect: "+str(score[0])+" Incorrect: "+str(score[1])
    bank.resetScore()
    return redirect(url_for('calculator',memoryBankScore=scoreDisplay))
    