import random #import random module

def generate_random_code(): #code generating method
    digits = list(range(10)) #create a list of digits from 0 to 9
    random.shuffle(digits) #shuffle the digits
    return digits[:3] #return the first three unique digits

def get_user_guess(): #method to get user input
    while True: #Loop until valid input is received
        guess = input("enter a 3-digit code with unique digits (no numbers repeat): ") #prompt user for input

        if len(guess) != 3:
            print("That's too many digits! Please enter exactly 3")
            continue #check if input is 3 digits long

        if not guess.isdigit():
            print("That is NOT a digit! Please enter only numbers!")
            continue

        if len(set(guess)) != 3:
            print("Oml, there are no repeat digits! Try again!")
            continue
        
        return [int(d) for d in guess] #return the input as a list of integers

def give_clues(code, guess):
    clues = []

    for i in range (len(guess)):
        if guess[i] == code[i]:
            clues.append("Match")
        elif guess [i] in code:
            clues.append("Close")
    
    if not clues:
        return["Nope"]
    
    return clues

def play_game():
    print("Welcome to Guess the Code!")
    print("I have generated a 3-digit code with unique digits.")
    print("Try to guess the code in 10 attempts or less! \n")

    secret_code = generate_random_code()
    attempts = 10

    while attempts > 0:
        print(f"You have {attempts} left to guess the code")
        guess = get_user_guess()
        clues = give_clues(secret_code, guess)
        print("Clues:", ', '.join(clues))
        print()

        if clues == ["Match", "Match", "Match"]:
            print("Congratulations! You've guessed the code!")
            break

        attempts -= 1
    else:
        print("Booo! You suck! All your guesses were wrong! The code was:", secret_code)


play_game()# start the game