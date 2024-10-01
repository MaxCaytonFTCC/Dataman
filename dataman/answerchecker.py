import functions as fn

def main():
    
    score = 0
    
    runProg = True
    
    while runProg:
        
        problem, answer = fn.answerChecker()
        print(f"What is: {problem}?\n")
        user_input = input("Enter your answer or 'E' to exit: \n")
        
        if user_input.upper() == 'E':
            
            runProg = False
        else:
            try:
                userAnswer = float(user_input)
                if fn.checkInput(problem, userAnswer):
                    print("Correct!")
                    score += 1
                else:
                    print(f"Incorrect. The correct answer is {answer}.")
            except ValueError:
                print("Invalid input. Please enter a number or 'E' to exit.")
    
    print(f"Your score is {score}!")

if __name__ == "__main__":
    main()
