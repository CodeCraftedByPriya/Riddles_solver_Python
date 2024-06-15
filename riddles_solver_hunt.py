import random

# Riddles dictionary
riddles = {
    "What has lots of eyes, but can't see? - 6 words": "potato",
    "What has one eye, but can't see? - 6 words": "needle",
    "What has hands, but can't clap? - 5 words": "clock",
    "What has legs, but doesn't walk? - 5 words": "table",
    "What has one head, one foot and four legs? - 3 words": "bed",
    "What can you catch, but not throw? - 4 words": "cold",
    "What has many teeth, but can't bite? - 4 words": "comb",
    "What has words, but never speaks? - 4 words": "book",
    "I’m tall when I’m young, and I’m short when I’m old. What am I? - 6 words": "candle",
    "What is always in front of you but can’t be seen? - 6 words": "future",
    "The poor have me; the rich need me. Eat me and you will die. What am I? - 7 words": "nothing",
    "What word contains all of the twenty-six letters? - 9 words": "alphabets",
    "What five-letter word can be read the same upside down or right side up?": "swims",
    "What has a head and a tail, but no body or legs? - 4 words": "coin",
    "What do you call a three-humped camel? - 8 words": "pregnant"
}

def difficulty_options() -> int:         #To selct the difficulty levels
    while True:
        try:
            difficulty = int(input("Choose difficulty (2 - High, 3 - Medium, 5 - Very Easy): "))
            if difficulty in (2, 3, 5):
                return difficulty
            else:
                print("Invalid difficulty. Please choose 2, 3, or 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    difficulty = difficulty_options()
    num_questions = 0
    correct_ans = 0

    if difficulty == 2:  # High difficulty               #alloting number of questions to the levels
        q = 10
        num_questions = 10
    elif difficulty == 3:  # Medium difficulty
        q = 7
        num_questions = 7
    elif difficulty == 5:  # Easy difficulty
        q = 5
        num_questions = 5

    lives = difficulty  # to choose the number of lives

    while lives > 0 and num_questions > 0:  # Randomly select a riddle from the dictionary
        riddle, answer = random.choice(list(riddles.items()))

        print(f"\nRiddle ({lives} lives remaining):\n{riddle}")
        user_ans = input("Your answer: ").lower()

        if user_ans == answer.lower():
            print("Correct! You move on to the next riddle.")
            del riddles[riddle]  # Remove solved riddle to avoid repetition
            num_questions -= 1
            correct_ans += 1     #count of number of correct answers
        else:
            lives -= 1
            num_questions -= 1
            print(f"Incorrect. The answer is: {answer}")

    if lives == 0:
        print(f"\nGame over! You ran out of lives.")
    elif num_questions == 0 and correct_ans == q:
        print("Congratulations! You Won!")
    else:
        print(f"Yesssss!!! You have completed this stage with {correct_ans} out of {q}")

#OPENING OF THE GAME
if __name__ == "__main__":
    print("WELCOME TO THE GAME OF CHOICES - RIDDLES HUNT")
    print("Enter 1 if you want to know HOW TO PLAY!\nEnter 2 if you want to START the game")
    strt = int(input())

    if strt == 1:                    #Rules for the game
        print("HERE ARE THE RULES:\n1. You will be asked to fill out the textbox with the answers for the riddles (No of words will be given), and you have lives according to the level you choose.\n2. Each time you choose a wrong option, you will loose a life.\n3. If you choose the right answer, you will be given the next question.")
        strt = 2

    if strt == 2:                    #The game starts
        print("THE GAME IS STARTING>>>")
        play_game()
