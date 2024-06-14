#RIDDLES SOLVER HUNT
import random

# Riddle dictionary (improved for clarity and efficiency)
riddles = {
    "What has lots of eyes, but can't see? - 6 words": "potato",
    "What has one eye, but can't see? - 6 words": "needle",
    "What has hands, but can't clap? - 5 words": "clock",
    "What has legs, but doesn't walk? - 5 words": "table",
    "What has one head, one foot, and four legs? - 3 words": "bed",
    "What can you catch, but not throw? - 4 words": "cold",
    "What has many teeth, but can't bite? - 4 words": "comb",
    "What has words, but never speaks? - 4 words": "book",
    "I’m tall when I’m young, and I’m short when I’m old. What am I? - 6 words": "candle",
    "What is always in front of you but can’t be seen? - 6 words": "future"
}

def difficulty_options():     #To let the user to choose a difficulty level.
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
    lives = difficulty    # to choose the number of lives
   
    if not riddles:  # Check if riddles dictionary is empty
        print("Congratulations! You Won!")
        return  # Exit the game if no riddles
    
    while lives > 0:      # Randomly select a riddle from the dictionary
        riddle, answer = random.choice(list(riddles.items()))

        print(f"\nRiddle ({lives} lives remaining):\n{riddle}")
        user_ans = input("Your answer: ").lower()

        if user_ans == answer.lower():
            print("Correct! You move on to the next riddle.")
            del riddles[riddle]  # Remove solved riddle to avoid repetition
        else:
            lives -= 1
            print(f"Incorrect. The answer is: {answer}")

    if lives == 0:
        print(f"\nGame over! You ran out of lives.")


if __name__ == "__main__":
    print("WELCOME TO THE GAME OF CHOICES - RIDDLES HUNT")
    print("Enter 1 if you want to know HOW TO PLAY!\nEnter 2 if you want to START the game")
    strt = int(input())
    if strt == 1:
        print("HERE ARE THE RULES:\n1. You will be asked to fill out the textbox with the answers for the riddles (No of words will be given), and you have lives according to the level you choose.\n2. Each time you choose a wrong option, you will loose a life.\n3. If you choose the right answer, you will be given the next question.")
        strt = 2
    if strt == 2:
        print("THE GAME IS STARTING>>>")
        play_game()
