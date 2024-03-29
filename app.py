# TODO: error handling:
# 1. invalid option for player_option
# 2. When letter is greater than 1.
# 3. When letter is "blank".
# NOTE: Generally, just need to refactor.

import random

##### functions:
def define_player_order():
  player1_name = input("Enter Player 1's name: ").upper()
  player2_name = input("Enter Player 2's name: ").upper()
  player3_name = input("Enter Player 3's name: ").upper()

  all_players = [player1_name, player2_name, player3_name]
  random.shuffle(all_players)
  print(f"The order of players will be {all_players[0]}, {all_players[1]}, then {all_players[2]}.\n")
  return all_players

def get_all_letters_of_puzzle(initial_list):
  final_list = []
  i = 0
  while i < len(initial_list):
    if initial_list[i] not in final_list:
      final_list.append(initial_list[i])
    i += 1
  return final_list

def count_number_of_letter_occurrance(puzzle_list, letter_list):
  count_list = []
  i = 0

  for x in letters_of_puzzle:  
    count_list.append(puzzle_list.count(letter_list[i]))
    i += 1
  return count_list

def find_number_of_letter(a_list, user_letter):
  for place in range(len(a_list)):
    if user_letter == a_list[place]:
      # Assigning place to index because in the for statement, it goes from 0 to len(a_list) so if
      # place is returned, it will always return the len(a_list) value  
      index = place
  return index


##### main program
game_on = True

while game_on == True:
  possible_puzzles = [ 
                      'disney world', 
                      'every rose has its thorn',
                      'national hockey league' 
                      ]

  consonants = [ 
                'B', 'C', 'D', 'F', 'G', 'H', 
                'J', 'K', 'L', 'M', 'N', 'P', 
                'Q', 'R', 'S', 'T', 'V', 'W', 
                'X', 'Y', 'Z'
               ]
  vowels = [ 'A', 'E', 'I', 'O', 'U' ]

  all_letters = consonants + vowels

  points = [ 
            '100', '100', '100', '100', '100', '100',
            '200', '200', '200', '200', '200', '200',
            '500', '500', '500', '750', '750', '750', 
            '1100', '5000'
           ]

  players_scores = [ 0, 0, 0 ]
  player_num = 0

  game_over = False
  player_turn = [ True, False, False ]

  player_options = f"""
  1. Spin the wheel.
  2. Buy a vowel.
  3. Solve the puzzle.
  """

  players = []
  letters_of_puzzle = []
  original_puzzle = []
  already_guessed = []

  # puzzle = input("Enter a word or a phrase for the puzzle.\n")
  puzzle = random.choice(possible_puzzles)
  puzzle_list = list(puzzle.upper())
  # This creates a duplicate of the list. In Python, both lists are pointing to the same object so if one is updated, both are updated.
  # Therefore, the "slice" method (:), needs to be used to create a copy of the list.
  # Reference: https://stackoverflow.com/questions/11993878/python-why-does-my-list-change-when-im-not-actually-changing-it
  original_puzzle = puzzle_list[:]

  letters_of_puzzle = get_all_letters_of_puzzle(puzzle_list)
  
  letter_count = count_number_of_letter_occurrance(puzzle_list, letters_of_puzzle)

  for space in range(len(puzzle_list)):
    if puzzle_list[space] == " ":
      puzzle_list[space] = "_"
    elif puzzle_list[space] in all_letters:
      puzzle_list[space] = " "
  print(f"Here is the puzzle:\n{puzzle_list}")
  # TODO: if time, display each word on a new line

  players = define_player_order()

  while game_over == False:
    while player_num < 3:
      while player_turn[player_num] == True:
        print(f"{players[player_num]}, would you like to:")
        print(player_options)
        player_choice = input()

        if int(player_choice) == 1:
          spin_points = random.choice(points)
          print(f"Letters already_guessed: {already_guessed}")
          letter = input(f"For {spin_points} points, which consonant would you like to choose?\n").upper()

          if letter in already_guessed:
            print(f"Sorry, {letter} has already been guessed.")

            # set_next_turn(player_turn, player_num)
            player_turn[player_num] = False
            if player_num < 2:
              player_turn[player_num + 1] = True
              player_num += 1
            else:
              player_num = 0
              player_turn[player_num] = True

          else:
            already_guessed.append(letter)

            if letter in consonants:
              if letter in original_puzzle:
                
                num_of_letter = find_number_of_letter(letters_of_puzzle, letter)
                print(f"Yes, there are {letter_count[num_of_letter]} {letter}s in the puzzle.")
                players_scores[player_num] += int(spin_points) * (letter_count[num_of_letter])
                print(f"{players[player_num]}'s score is {players_scores[player_num]}.")

                for cnsnt in range(len(original_puzzle)):
                  if original_puzzle[cnsnt] == letter:
                    puzzle_list[cnsnt] = letter
                print(f"Here is the puzzle:\n{puzzle_list}")
              else:
                print(f"I'm sorry, there are no {letter}s.")

                player_turn[player_num] = False
                if player_num < 2:
                  player_turn[player_num + 1] = True
                  player_num += 1
                else:
                  player_num = 0
                  player_turn[player_num] = True
            else: 
              print(f"I'm sorry. {letter} is not a consonant.")
          
              # set_next_turn(player_turn, player_num)
              player_turn[player_num] = False
              if player_num < 2:
                player_turn[player_num + 1] = True
                player_num += 1
              else:
                player_num = 0
                player_turn[player_num] = True

        elif int(player_choice) == 2:

          if players_scores[player_num] < 200:
            print(f"I'm sorry, you do not have the minimum 200 points score needed to buy a vowel. Please choose another option. ")
            player_choice = input(player_options)
          else:
            print(f"Letters already_guessed: {already_guessed}")
            letter = input("Which vowel would you like to choose?\n").upper()

            if letter in already_guessed:
              print(f"Sorry, {letter} has already been guessed.")

              # set_next_turn(player_turn, player_num)
              player_turn[player_num] = False
              if player_num < 2:
                player_turn[player_num + 1] = True
                player_num += 1
              else:
                player_num = 0
                player_turn[player_num] = True
            else:
              already_guessed.append(letter)

              if letter in vowels:

                if letter in original_puzzle:
                  num_of_letter = find_number_of_letter(letters_of_puzzle, letter)
                  print(f"Yes, there are {letter_count[num_of_letter]} {letter}s in the puzzle.")
                  players_scores[player_num] -= 200
                  print(f"{players[player_num]}'s score is {players_scores[player_num]}.")

                  for vwl in range(len(original_puzzle)):
                    if original_puzzle[vwl] == letter:
                      puzzle_list[vwl] = letter
                  print(f"Here is the puzzle:\n{puzzle_list}")
                else:
                  print(f"I'm sorry, there are no {letter}s.")

                  # set_next_turn(player_turn, player_num)
                  player_turn[player_num] = False
                  if player_num < 2:
                    player_turn[player_num + 1] = True
                    player_num += 1
                  else:
                    player_num = 0
                    player_turn[player_num] = True
              else: 
                print(f"I'm sorry. {letter} is not a vowel.")
                
                # set_next_turn(player_turn, player_num)
                player_turn[player_num] = False
                if player_num < 2:
                  player_turn[player_num + 1] = True
                  player_num += 1
                else:
                  player_num = 0
                  player_turn[player_num] = True

        elif int(player_choice) == 3:
          puzzle_attempt = input("What is the puzzle?\n")
          if puzzle_attempt.upper() == puzzle.upper():
            print(f"Congratulations {players[player_num]}! You solved the puzzle: {puzzle}")
            print(f"{original_puzzle}")
            # Adding three to kick out of the while player_num < 3 loop
            player_num += 3
            game_over = True
            break
          else:
            print(f"I'm sorry, {players[player_num]}, that is incorrect.")
            player_turn[player_num] = False
            if player_num < 2:
              print(f"{players[player_num + 1]}, it is your turn.")
              player_turn[player_num + 1] = True
              player_num += 1
            else:
              player_num = 0
              print(f"{players[player_num]}, it is your turn.")
              player_turn[player_num] = True
          break
        else:
          print("Please select a valid option.")
          player_choice = input(player_options)

  play_again = input("Would you like to play again? Y | N ")
  if play_again.upper() == "Y":
    game_over = False
  elif play_again.upper() == "N":
    break;
  else:
    print("Please select a valid option.")
    play_again = input("Would you like to play again? Y | N ")
