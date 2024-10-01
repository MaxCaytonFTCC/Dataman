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
