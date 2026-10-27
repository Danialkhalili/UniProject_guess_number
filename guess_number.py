
import random


# YOUR CHANSCES
MAX_ATTEMPTS = 5


def generate_number():
    """
    MAKE A RANDOM NUMBER BETWEEN 1 TO 100
    """
    return random.randint(1, 100)


def get_valid_guess():
    """
    GET THE INPUT AND CHECK IF IT`S VALID OR NOT
    """

    while True:
        user_input = input("ENTER YOUR GUESS :")

        # CHEK THE INPUT (INTEGER ONLY)
        if not user_input.isdigit():
            print("INVALID INPUT PLEASE ENTER AN INTEGER.")
            continue

        guess = int(user_input)

        # CHECK THE RANGE
        if guess < 1 or guess > 100:
            print("NUMBER SHOULD BE IN 1 TO 100.")
            continue

        # IF THE INPUT IS VALID
        return guess


def show_hint(guess, secret_number):
    """
    GIVE YOU A HINT THAT HOW FAR YOU ARE
    """

    difference = abs(guess - secret_number)

    # CHECK THE GUESS DIRECTION
    if guess < secret_number:
        print("NUMBER IS BIGGER. GUESS A BIGGER NUMBER!")

    elif guess > secret_number:
        print("NUMBER IS SMALLER. GUESS A SMALLER NUMBER!")

    # CHECK HOW FAR YOU ARE
    if difference <= 5:
        print("TOO CLOSE!")

    elif difference <= 15:
        print("CLOSE BUT ESTIL FAR!")

    else:
        print("TOO FAR!")


def get_rank(attempt):
    """
    GIVA THE PLAYER RABK
    """

    ranks = {
        1: "GREAT! FIRST TRY.",
        2: "VERY GOOD!WIN IN SECOND TRY.",
        3: "GOOD! WIN IN THIRD TRY.",
        4: "ACCEPT! YOU WIN.",
        5: "YOU WERE LUCKY THIS TIME."
    }

    return ranks[attempt]


def play_game():
    """
    RUN 1 ROUND OF A GAME
    """

    secret_number = generate_number()

    attempts = 0

    print("\n==============================")
    print("      GUESS THE NUMBER")
    print("==============================")
    print("THERE IS NUMBER BETWEEN 1 TO 100.")
    print("\nYOU HAVE 5 CHANCE TO GUESS IT.")

    # LOOP UNTIL YOU LOSE
    while attempts < MAX_ATTEMPTS:

        # VALID GUESS
        guess = get_valid_guess()

        # ONLY VALID GUESS MAKE IT INCREASE
        attempts += 1

        remaining_attempts = MAX_ATTEMPTS - attempts

        # SHOW YOUR ATTEND AND CHANSES
        print(f"\n{attempts}TRY FROM {MAX_ATTEMPTS}")
        print(f"CHANCES: {remaining_attempts}")

        # CHACK THE CORRECT GUESS
        if guess == secret_number:

            print("\ncongratulations! YOU GUESS THE NUMBER.")

            # SHOW PLAYER RANK
            print(get_rank(attempts))

            return

        # IF YOUR GUESS WAS WRONG
        show_hint(guess, secret_number)

    # IF YOU LOSSE
    print("\nSORRY YOU LOST!")
    print(f"THE NUMBER WAS {secret_number}.")


def ask_play_again():
    """
    ASK IF YOU WANT TO PLAY AGAIN
    """

    while True:

        answer = input("\nDO YOU WANT TO PLAY AGAIN? (PLEASE ENTER YES OR NO): ")

        answer = answer.strip().lower()

        if answer == "yes":
            return True

        elif answer == "no":
            return False

        else:
            print("PLEASE ENTER YES OR NO.")


def main():
    """
    MANAGMENT
    """

    while True:

        # ON ROUND OF GAME
        play_game()

        # SEE IF YOU WANT TO PLAY AGAIN
        if not ask_play_again():
            print("\nIT WAS NICE TO PLAY WITH YOU!")
            print("END.")
            break


# MAIN
if __name__ == "__main__":
    main()
