import random

ALPHABET_LIST = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


# This function selects a word at random from the file it is passed
def choose_random_word(file):
    # open and read the file
    with open (file, 'r') as reader:
        open_doc = reader.read()
    # with new string convert it to a list of strings all upper case
    new_list = open_doc.upper().split()
    # print(new_list)
    # choose a random word based on the index in the new list
    answer = new_list[random.randint(0, len(new_list))]
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


# Play the game
def play_game(file):
    answer = choose_random_word(file)
    print(answer)
    answer_list = create_answer_list(answer)
    print(answer_list)
    guess = accept_user_guess()
    print(guess)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        play_game(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
    
