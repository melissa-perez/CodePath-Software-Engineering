
# adding random library
import random
from hangman_words import word_list
from hangman_art import logo, stages
word_list_length = len(word_list)
is_replay = 'y'

while is_replay == 'y':
  end_of_game = False
  lives = 6

  # print the logo
  print(logo)
  # pick a word
  chosen_word = random.choice(word_list)
  chosen_word_length = len(chosen_word)

  # create display array
  display_ui_list = ['_'] * chosen_word_length
  guessed_letters = []

  while not end_of_game:
    # tell user to guess
    user_guess = input('Please guess a single letter: ').lower()
    
    if user_guess not in guessed_letters:
      guessed_letters.append(user_guess)

      if user_guess not in chosen_word:
        if lives > 0: 
          lives -= 1
          print(f'Lost a life, {lives} remain. The letter {user_guess} is not in the word.')
      
          if lives == 0:
            print('You lose.')
            end_of_game = True
      else:  
        for i in range(chosen_word_length):
          if chosen_word[i] == user_guess:
            display_ui_list[i] = user_guess
      
        if '_' not in display_ui_list:
          print('You win!')
          end_of_game = True
    else:
        print(f'You already guessed the letter {user_guess}.')
    
    # print display list
    print(f"{' '.join(display_ui_list)}")
    print(stages[lives])

  print(f"The word was {chosen_word}.")

  is_replay = input('Would you like to play again? Enter y: ').lower()
  