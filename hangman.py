import random
from string import ascii_lowercase

words = ['python', 'java', 'kotlin', 'javascript']
menu = ''
print('H A N G M A N')
while menu != 'exit':
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == 'play':
        word = random.choice(words)
        word_set = set(word)
        dashed_word = list('-' * len(word))
        pressed_letters_set = set()

        mistakes = 0
        while mistakes < 8:
            print('\n' + ''.join(dashed_word))
            if dashed_word.count('-') == 0:
                break
            input_letter = input('Input a letter: ')
            if input_letter in pressed_letters_set:
                print("You've already guessed this letter")
            else:
                if len(input_letter) != 1:
                    print("You should input a single letter")
                elif input_letter not in ascii_lowercase:
                    print("Please enter a lowercase English letter")
                else:
                    pressed_letters_set.add(input_letter)
                    if input_letter in word_set:
                        if input_letter not in dashed_word:
                            for letter in enumerate(word):
                                if input_letter == letter[1]:
                                    dashed_word[letter[0]] = input_letter
                        else:
                            print("No improvements")
                            mistakes += 1
                    else:
                        print("That letter doesn't appear in the word")
                        mistakes += 1
        print('''You guessed the word!
You survived!\n''' if mistakes < 8 else 'You lost!\n')
