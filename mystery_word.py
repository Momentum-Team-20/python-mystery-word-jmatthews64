import random

game_on = True


# Function to allow the user to select a level and validate the selection
def select_level():
    level = input("1. (Easy), 2. (Medium), 3. (Hard): ")
    level_list = ['1', '2', '3']
    if level in level_list:
        return level
    else:
        print("Please select 1, 2, or 3.")
        corrected_level = select_level()
        return corrected_level


# This function selects a word at random from the file it is passed
def choose_random_word(file, level):
    # open and read the file
    with open (file, 'r') as reader:
        open_doc = reader.read()
    # with new string convert it to a list of strings all upper case
    new_list = open_doc.upper().split()
    # Create word lists for each level
    easy_level_list = [word for word in new_list if len(word) < 7 and len(word) > 3]
    medium_level_list = [word for word in new_list if len(word) < 9 and len(word) > 5]
    hard_level_list = [word for word in new_list if len(word) > 7]
    # choose a random word based on the index in the new list and level
    if level == "1":
        answer = easy_level_list[random.randint(0, len(easy_level_list))]
    elif level == "2":
        answer = medium_level_list[random.randint(0, len(medium_level_list))]
    else:
        answer = hard_level_list[random.randint(0, len(hard_level_list))]
    return answer


# This function will recieve and validate user input to pass back for valuation against the answer
def accept_user_guess():
    user_guess = input("Please guess a letter: ").upper()
    if len(user_guess) == 1 and user_guess.isalpha():
        return user_guess
    else:
        print("Please guess only 1 letter at a time")
        corrected_guess = accept_user_guess()
        return corrected_guess


# This function will take the answer and make it into a list of characters
def create_answer_list(answer):
    new_list = []
    for character in answer:
        new_list.append(character)
    return new_list


# Convert the mystery word to a string of space separated underscores
def convert_answer(answer):
    answer_length = len(answer)
    new_display = []
    while answer_length > 0:
        new_display.append("_ ")
        answer_length -= 1
    new_display_string = ""
    for each in new_display:
        new_display_string += each
    return new_display_string


# Function that will check to see if the letter has already been guessed
def has_been_guessed(guess):
    if guess not in already_guessed:
        already_guessed.append(guess)
        return guess
    else:
        print("You've already guessed: ", guess)
        print(" ")
        new_guess = accept_user_guess()
        not_guessed = has_been_guessed(new_guess)
        return not_guessed


# Create a function to validate if the guess is correct
def is_correct(guess, answer_list, display_list):
    if guess in answer_list:
        print("Correct!")
        new_list = display_list.split()
        # Find the index values of the correct letter
        guess_indexes = [i for i in range(len(answer_list)) if answer_list[i] == guess]
        # Convert indices into int()
        for j in range(0,len(guess_indexes)):
            guess_indexes[j] = int(guess_indexes[j])
        # Replace the values at correct indices in new_list
        for each in guess_indexes:
            new_list[each] = (guess)
        # Create new string to display for the user with updated charaters and return it
        new_display = ""
        for each in new_list:
            new_display += f"{each} "
        return new_display
    else:
        print("Incorrect!")
        return display_list
    

# Update the guess count on an incorrect guess
def update_guess_count(guess_count, answer_list, guess):
    if guess not in answer_list:
        guess_count -= 1
    return guess_count


# Function to run game again
def keep_playing():
    play_again = input("Do you want to play again (Y or N)? ")
    play_again = play_again.upper()
    if play_again == "N":
        print("Goodbye!")
        quit()


# Play the game
def play_game(file):
    print("What difficulty would you like?")
    validated_level = select_level()
    guess_count = 8
    print("Incorrect Guesses Remaining: ", guess_count)
    answer = choose_random_word(file, validated_level)
    answer_list = create_answer_list(answer)
    new_answer_display = convert_answer(answer_list)
    print(new_answer_display)
    updated_display = new_answer_display
    # Loop through the interface until all letters guessed or guess_count = 0
    while '_' in updated_display and guess_count != 0:
        guess = accept_user_guess()
        not_guessed = has_been_guessed(guess)
        updated_display = is_correct(not_guessed, answer_list, updated_display)
        print(updated_display)
        guess_count = update_guess_count(guess_count, answer_list, not_guessed)
        print("Incorrect guesses remaining: ", guess_count)
        print(" ")
    if guess_count == 0:
        print("You lose!  The correct word was: ", answer)
    else:
        print("You win!  The answer was: ", answer)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        while game_on == True:
            already_guessed = []
            play_game(file)
            keep_playing()
    else:
        print(f"{file} does not exist!")
        exit(1)
