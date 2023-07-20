"""
below is a guess game between either two players
or between a player and a computer or a demo practice
for a new player.
# game type
    -two players - (meaning two individuals are playing the game against each other)
    - one player - (meaning an individual is playing against the computer)
    - practice - aids a new person(an amateur) to practice and understand the game
# defining the rules
    - the game is played for the agreed number of rounds
    - each player makes the agreed number of guess
    - if a player makes the right guess on first attempt they get 2 points
      otherwise they get 1 point for making the right the right guess and finally they
      get 0 points if they are out of guesses and having not made the right guess

# variables
    1. guess_limit - the maximum number of guess a player can make in a particular round
    2. Total_points -  totals points scored by each player
    3. number_of_guess
    4. game_type - practice, one_player and two_player
    5. number_of_games -
    6. player_1 and player_2
    7. secret_word and guess
# other dynamics to implement in the game
    - the players can choose to play the game either  by guessing numerals or stings(statements inclusive)
    - a player can ask for a clue
    - game level(easy, medium, hard) in case you're playing against the computer
"""
import random


def show_player_outcome(secret_word):
    number_of_guesses = 0
    guess_limit = 5
    outcome = ""

    while number_of_guesses < guess_limit:
        players_guess = input("Enter your guess here: ").lower()
        number_of_guesses += 1
        if players_guess != secret_word:
            trials = guess_limit - number_of_guesses
            if trials == 1:
                print("Wrong guess, last trial!!!")
            elif trials == 0:
                outcome = "lose"
            else:
                print(f"Wrong guess, {trials} trials remaining")
        else:
            outcome = "win"
            number_of_guesses = guess_limit
    return outcome


def show_computer_outcome(secret_word):
    number_of_guesses = 0
    guess_limit = 5
    outcome = ""
    computer_guesses = ["mouse", "keyboard", "printer", "monitor", "touchpad", "motherboard", "bios", "usb",
                        "speaker", "microphone", "wifi adapter", "cables", "screen", "cpu", "camera", "webcam",
                        "ram", "rom", "video card", "headphones", "sound card", "hard disk", "ups", "microprocessor"]
    while number_of_guesses < guess_limit:
        computers_guess = random.choice(computer_guesses)
        number_of_guesses += 1
        if computers_guess != secret_word:
            trials = guess_limit - number_of_guesses
            if trials == 0:
                outcome = "lose"
        else:
            outcome = "win"
            number_of_guesses = guess_limit
    return outcome


