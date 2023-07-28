# @thesalmanpk

import random

print("Welcome to Basic Python Tools! \nDeveloped by M. Salman Iqbal. \n")

def game():
    print(". \n================= \nGUESS NUMBER GAME \n================= \n")
    print("I have a number in my mind. \nCan you guess the number? \n")
    num = random.randint(1,99)
    cycles = 0
    while True:
        cycles = cycles + 1
        guess = input("Enter your guess in range 1 to 99: ")
        if int(guess) == num: 
            print("================== \nYayyy! You WON !!! \n================== \n\nYou guessed the right number in (" + str(cycles) + ") attempts. \nI also thought the number " + str(num) + ". \n\n")
            break
        if int(guess) < num:
            print("You guessed a lower number. Try Again! \n")
        if int(guess) > num:
            print("You guessed a higher number. Try Again! \n")



def compete():
    print(". \n================= \nGUESS NUMBER GAME \n================= \n")
    me = "Salman"
    a = 1
    b = 99
    print(f"Computer have selected a number between {a} and {b}. \nType your guess below. Try to guess before {me}. \n")
    num = random.randint(a, b)
    loops = 0
    while True:
        loops = loops + 1
        guess = input(f"Guess number from {a} to {b}: ")
        guess = int(guess)
        computerguess = random.randint(a, b)
        print(f"You guessed: ({guess}) | {me} guessed: ({computerguess}). \n")
        
        if guess < num and computerguess != num:
            a = guess + 1
            print("Your guess is smaller than the number. Try Again! \n")
        if guess > num and computerguess != num:
            b = guess - 1
            print("Your guess is greater than the number. Try Again. \n")
        
        if guess == num and computerguess != num:
            print("")
            print(f"=========== \nYou WON! \n=========== \nGuess {guess} matched with num ({num}) in {loops} attempts. \n\n")
            break
        if computerguess == num and guess != num:
            print("")
            print(f"=========== \n{me} WON! \n=========== \nGuess {computerguess} matched with num ({num}) in {loops} attempts. \n\n")
            break
        if guess == num and computerguess == num:
            print("")
            print(f"=========== \nMATCH DRAW! \n=========== \n\n")
            compete()
            break


def vs():
    a = input("Type a smaller number for range: ")
    a = int(a)
    b = input("Type a greater number for range: ")
    b = int(b)
    player1 = input("Enter player 1 name: ")
    player2 = input("Enter player 2 name: ")
    print(f"================================================= \n{player1} vs {player2} | playing Guess {a}-{b} Number Game. \n=================================================    \n")
    loops = 0
    num = random.randint(a, b)
    while True:
        loops = loops + 1
        guess = random.randint(a, b)
        guess2 = random.randint(a, b)
        print(f"{player1} guessed: ({guess}) | {player2} guessed ({guess2})")
        
        # Update the range based on player 1's guess
        if guess < num:
            a = guess + 1
        if guess > num:
            b = guess - 1
    
        # Update the range based on player 2's guess
        if guess2 < num:
            a = guess2 + 1
        if guess2 > num:
            b = guess2 - 1
        
        if guess == num and guess2 != num:
            print("")
            print(f"=========== \n{player1} WON! \n=========== \nGuess {guess} matched with num ({num}) in {loops} attempts. \n\n")
            break
        if guess2 == num and guess != num:
            print("")
            print(f"=========== \n{player2} WON!. \n=========== \nGuess {guess2} matched with num ({num}) in {loops} attempts. \n\n")
            break
        if guess == num and guess2 == num:
            print("")
            print(f"=========== \nMATCH DRAW! \n=========== \n\n")
            vs()
            break


def pypractice():
    print("================================ \nWelcome to Python Code Practice! \n================================ \n\nEnter Python code to see results. \nNote: This only works for 01 line code. \n")
    while True:
        code = input("Write Code: ")
        try:
            result = eval(code)
            print(" ")
            break
        except Exception as e:
            print("Error:", e)

def tools():
    print("=========================================== \nSelect a tool from following list to start. \n=========================================== \n")
    while True:
        tool = input("Enter (1) for Calculator \nEnter (2) for Text Bomber \nEnter (3) for Guess Number Game \nEnter (4) for Python Code Practice \nEnter (5) for Guess Num Game (Compete with Salman) \nEnter (6) for Guess Number Game (Luck Checker) \n\nEnter number: ")
        if tool == "1":
            print("====================== \nWelcome to Calculator! \n====================== \n\nWhat do you want to do?")
            while True:
                task = input("Type (D) for Division \nType (M) for Multiplication \nType (A) for Addition \nType (S) for Substraction \n\nType here: ")
                if task == "D" or task == "d" or task == "M" or task == "m" or task == "A" or task == "a" or task == "S" or task == "s":
                    a = input("Type your first number: ")
                    b = input("Type your second number: ")
                    if task == "D" or task == "d":
                        ans = int(a) / int(b)
                        print("Answer: " + str(ans))
                        action = input("Task Completed! \n(1) for Restart | (2) for Exit: ")
                        if action == "1":
                            tools()
                        else:
                            print("Thankyou for using Basic Python Tools! \nGive Feedback on 0309-9983028 :)")
                            break
                        break
                    if task == "M" or task == "m":
                        ans = int(a) * int(b)
                        print("Answer: " + str(ans))
                        action = input("Task Completed! \n(1) for Restart | (2) for Exit: ")
                        if action == "1":
                            tools()
                        else:
                            print("Thankyou for using Basic Python Tools! \nGive Feedback on 0309-9983028 :)")
                            break
                        break
                    if task == "A" or task == "a":
                        ans = int(a) + int(b)
                        print("Answer: " + str(ans))
                        action = input("Task Completed! \n(1) for Restart | (2) for Exit: ")
                        if action == "1":
                            tools()
                        else:
                            print("Thankyou for using Basic Python Tools! \nGive Feedback on 0309-9983028 :)")
                            break
                        break
                    if task == "S" or task == "s":
                        ans = int(a) - int(b)
                        print("Answer: " + str(ans))
                        action = input("Task Completed! \n(1) for Restart | (2) for Exit: ")
                        if action == "1":
                            tools()
                        else:
                            print("Thankyou for using Basic Python Tools! \nGive Feedback on 0309-9983028 :)")
                            break
                        break
                else:
                    print("Invalid Entry! \n")
            break
        if tool == "2":
            text = input("======================= \nWelcome to Text Bomber! \n======================= \n\nType your text: ")
            bomb = input("How many times you want to multiply? \nEnter a number: ")
            text = text + " "
            print(text * int(bomb))
            action = input("Task Completed! \n(1) for Restart | (2) for Exit: ")
            if action == "1":
                tools()
            else:
                print("Thankyou for using Basic Python Tools! \nGive Feedback on 0309-9983028 :)")
                break
            break
        if tool == "3":
            game()
            action = input("Task Completed! \n(1) for Restart | (2) for Exit: ")
            if action == "1":
                tools()
            else:
                print("Thankyou for using Basic Python Tools! \nGive Feedback on 0309-9983028 :)")
                break
            break
        if tool == "4":
            pypractice()
            action = input("Task Completed! \n(1) for Restart | (2) for Exit: ")
            if action == "1":
                tools()
            else:
                print("Thankyou for using Basic Python Tools! \nGive Feedback on 0309-9983028 :)")
                break
            break
        if tool == "5":
            compete()
            action = input("Task Completed! \n(1) for Restart | (2) for Exit: ")
            if action == "1":
                tools()
            else:
                print("Thankyou for using Basic Python Tools! \nGive Feedback on 0309-9983028 :)")
                break
            break
        if tool == "6":
            print(". \n================= \nGUESS NUMBER GAME \n================= \n")
            vs()
            action = input("Task Completed! \n(1) for Restart | (2) for Exit: ")
            if action == "1":
                tools()
            else:
                print("Thankyou for using Basic Python Tools! \nGive Feedback on 0309-9983028 :)")
                break
            break
        else:
            print("Tool Not Available! \n")

def login():
    print("================== \nLogin to continue. \n================== \n")
    while True:
        username = input("Enter username: ")
        if username.lower() == "salmaniqbal" or username == "":
            while True:
                password = input("Enter password: ")
                if password.lower() == "thesalmanpk" or password == "":
                    print("Login Successful! \n")
                    tools()
                    break
                else:
                    print("Wrong Password! \n")
            break
        else:
            print("User Not Found! \n")
            
login()