import random
import time

notinword = []
inword = []
guess = None
attempts = 0
words = [
    'apple', 'banana', 'orange', 'grape', 'peach', 'strawberry', 'melon',
    'kiwi', 'pear', 'plum'
]
print('''________   ___   _   ___   _   _ _____ 
| ___ \\ \\ / / | | | / _ \\ | \\ | |  __ \\
| |_/ /\\ V /| |_| |/ /\\_\\ \\|  \\| | |  \\/
|  __/  \\ / |  _  ||  _  || . ` | | __ 
| |     | | | | | || | | || |\\  | |_\\ \\
\\_|     \\_/ \\_| |_|\\_| |_|\\_| \\_/\\____/''')

print('HANGMAN IN PYTHON')
random_word = random.choice(words)
while guess != random_word:
  print('LETTERS IN WORD:')
  print(inword)
  print('LETTERS NOT IN WORD:')
  print(notinword)
  print('ATTEMPT No.')
  print(attempts)
  guess = input("Guess a letter: ").lower()
  if guess == random_word:
    print("You guessed the word!")
    print('In '+ str(attempts) +' attempts!')
    break
  elif len(guess) != 1:
    print("INCORRECT. Game over.")
    print('The word was:')
    print(random_word)
    break
  elif guess in random_word:
    print('That letter is in the word!')
    inword.append(guess + " ")
  elif guess not in random_word:
    print('That letter is not in the word')
    notinword.append(guess + " ")
  attempts += 1
  print('')
  print('')
  print('')
  print('')
  print('')
  print('')
  print('')
  print('')
  print('')
  print('')