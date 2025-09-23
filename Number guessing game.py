import random
EASY_LEVEL_RETURN = 10
HARD_LEVEL_RETURN = 5

def choose_difficulty(level):
    level = level.lower()   # fix: handle 'Easy' or 'easy'
    if level == "easy":
        return EASY_LEVEL_RETURN 
    elif level == "hard":
        return HARD_LEVEL_RETURN
    else:
        return None
    
def check_answer(guessed_number, answer, Attempts):
    if guessed_number < answer:
        print("Too Low")
        return Attempts - 1
    elif guessed_number > answer:
        print("Too High")
        return Attempts - 1
    else:
        print(f"You got it!!! The answer was {answer}")
        return Attempts

def fun_game():
    print("Welcome to the Number Guessing Game!")
    answer = random.randint(1, 50)
    level = input("Choose a difficulty level... 'Easy' or 'Hard': ")
    Attempts = choose_difficulty(level)
    guessed_number = 0
    
    while guessed_number != answer:
        if Attempts == 0:
            print("You've run out of guesses, you lose.")
            return
        print(f"You have {Attempts} attempts remaining to guess the number.")
        guessed_number = int(input("Make a guess: "))
        Attempts = check_answer(guessed_number, answer, Attempts)
        if guessed_number != answer and Attempts > 0:
            print("Guess again.")

fun_game()
