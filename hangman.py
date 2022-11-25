import random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
BOARD_STAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']

def find_indices(letters, guess):
    indices = []
    for idx, value in enumerate(letters):
        if value == guess:
            indices.append(idx)
    return indices

def game(difficulty):
    try:
        with open('./difficulties/{}.txt'.format(difficulty)) as f:
            word = random.choice(f.readlines())
    except FileNotFoundError:
        print('Invalid difficulty')
        return

    STRIKES = 0
    GUESSES = []

    word_letters = list(word)
    found_letters = ('_ ' * len(word_letters)).split(' ')[:-2]

    while 1:
        print("\033c", end='')
        print('Word: ' + ' '.join([str(e) for e in found_letters]) + '\nStrikes: ' + str(STRIKES) + '\nGuesses: ' + ' '.join([str(e) for e in GUESSES]) + '\n' + BOARD_STAGES[STRIKES])
        guess = input("Guess a letter: ").lower()
        if guess == word.strip():
            print("\033c", end='')
            print('Word: ' + ' '.join([str(e) for e in list(word)]) + '\nStrikes: ' + str(STRIKES) + '\nGuesses: ' + ' '.join([str(e) for e in GUESSES]) + '\n' + BOARD_STAGES[STRIKES])
            print('You win!')
            return
        elif len(guess) < 1:
            print("\033c", end='')
            input("Enter only 1 letter or what you think the word is. Press enter to continue...")
            continue
        elif guess in GUESSES:
            print("\033c", end='')
            input("You already guessed that letter! Press enter to continue...")
            continue
        elif len(guess) == 1 and guess not in LETTERS:
            print("\033c", end='')
            input("Only enter letters! Press enter to continue...")
            continue

        positions = find_indices(word_letters, guess)

        if positions == []:
            STRIKES += 1
            GUESSES.append(guess)
            if STRIKES == 6:
                print("\033c", end='')
                print("You lose!\nThe word was: " + word)
                break
        else:
            for position in positions:
                found_letters[position] = guess

        if '_' not in found_letters:
            print("\033c", end='')
            print("You win!\nThe word was: " + word)
            break

game(input('Difficulty (easy, medium, hard, extreme, or impossible): '))