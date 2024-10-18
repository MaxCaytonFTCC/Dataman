
# Equation Log
def addTolog(equation : str):
    log = open("memory_bank_log.txt","a")
    log.write(equation+'\n')
    log.close()

def addEquationsToLog(equations):
    log = open("memory_bank_log.txt","a")
    log.writelines(equations)
    log.close()

def getEquations():
    log = open("memory_bank_log.txt")
    equations = log.readlines()
    log.close()
    return equations

def getEquationCount():
    return len(getEquations())

def popNextEquation():
    # Get Current Equations
    currentEquations = getEquations()
    nextEquation = currentEquations.pop(0)
    clearLog()
    addEquationsToLog(currentEquations)
    return nextEquation

def clearLog():
    log = open("memory_bank_log.txt","a")
    log.truncate(0)
    log.close()

def isValidEquation(equation : str) -> bool:
    if (equation[-1] != '='): return False
    expression = equation.split('=')[0]
    try:
        eval(expression)
    except:
        return False
    return True

# Score
def recordAnswer(correct : bool):
    score = open("memory_bank_score.txt")
    lines = score.readlines()

    if (len(lines) <= 0):
        lines = ["0:0"]

    currentScores = lines[0].split(':')
    score.close()

    resetScore()

    score = open("memory_bank_score.txt","a")
    if (correct):
        newCorrect = str(int(currentScores[0]) + 1)
        score.write(newCorrect+":"+currentScores[1])
    else:
        newIncorrect = str(int(currentScores[1]) + 1)
        score.write(currentScores[0]+":"+newIncorrect)
    score.close()

def getScore():
    score = open("memory_bank_score.txt")
    lines = score.readlines()
    if (len(lines) <= 0):
        score.close()
        return [0,0]
    score.close()
    return lines[0].split(':')

def resetScore():
    score = open("memory_bank_score.txt","a")
    score.truncate(0)
    score.close()