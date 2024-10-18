import random

def answerChecker():
    operators = ['+', '-', '*', '/']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(operators)
    problem = f"{num1} {operation} {num2}"
    answer = eval(problem)
    return problem, answer

def checkInput(problem, userAnswer):
    correctAnswer = eval(problem)
    return userAnswer == correctAnswer

def checkAnswer(problemString : str) -> bool:
    # Split Problem by Equal Sign
    splitProblem = problemString.split('=')
    if (len(splitProblem) != 2): return False # Early rejection if unexpected length

    # Attempt to evaluate problem    
    try:
        if (splitProblem[1].isnumeric() == False): return False
        return checkInput(splitProblem[0],int(splitProblem[1]))
    except:
        return False