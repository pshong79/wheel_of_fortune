#### I think there are currently three things left to do:
# 1. figure out how to manage turns for players.
# 2. score keeping for correct letters.
# 3. score keepting for solving puzzle.

import random

##### functions:
def define_player_order():
  player1_name = input("Enter Player 1's name: ")
  player2_name = input("Enter Player 2's name: ")
  player3_name = input("Enter Player 3's name: ")

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

  player1_score = 0
  player2_score = 0
  player3_score = 0

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

  # puzzle = input("Enter a word or a phrase for the puzzle.\n")
  puzzle = random.choice(possible_puzzles)
  puzzle_list = list(puzzle.upper())
  # This creates a duplicate of the list. In Python, both lists are pointing to the same object so if one is updated, both are updated.
  # Therefore, the "slice" method (:), needs to be used to create a copy of the list.
  original_puzzle = puzzle_list[:]

  # delete during clean up
  print(f"puzzle_list {puzzle_list}")
  print(f"original_puzzle {original_puzzle}")
  letters_of_puzzle = get_all_letters_of_puzzle(puzzle_list)
  # delete during clean up
  print(letters_of_puzzle)
  
  letter_count = count_number_of_letter_occurrance(puzzle_list, letters_of_puzzle)
  # delete during clean up
  print(letter_count)

  for space in range(len(puzzle_list)):
    if puzzle_list[space] == " ":
      puzzle_list[space] = "_"
    elif puzzle_list[space] in all_letters:
      puzzle_list[space] = " "
  print(f"Here is the puzzle:\n{puzzle_list}")
  # TODO: if time, display each word on a new line

  players = define_player_order()

  # TODO: need to assign flags to players to manage whose turn it is. 

  while game_over == False:
    print(f"{players[0]}, would you like to:")
    player_choice = input(player_options)

    if int(player_choice) == 1:
      spin_points = random.choice(points)
      letter = input(f"For {spin_points} points, which consonant would you like to choose?\n").upper()

      if letter in consonants:
        print(f"letter {letter}")
        print(f"original_puzzle {original_puzzle}")
        if letter in original_puzzle:
          print(f"{letter} is in the puzzle.")

          for cnsnt in range(len(original_puzzle)):
            if original_puzzle[cnsnt] == letter:
              puzzle_list[cnsnt] = letter
          print(f"Here is the puzzle:\n{puzzle_list}")
          # TODO: show the puzzle
          # TODO: change print statement to say "Yes, there is/are X {letter}(s)"
          # TODO: add X * spin_points to player's total points
        else:
          print(f"I'm sorry, there are no {letter}s.")
      else: 
        print(f"I'm sorry. {letter} is not a consonant.")

    elif int(player_choice) == 2:
      letter = input("Which vowel would you like to choose?\n").upper()

      if letter in vowels:
        print(f"letter {letter}")
        print(f"original_puzzle {original_puzzle}")
        if letter in original_puzzle:
          print(f"{letter} is in the puzzle.")

          for vwl in range(len(original_puzzle)):
            if original_puzzle[vwl] == letter:
              puzzle_list[vwl] = letter
          print(f"Here is the puzzle:\n{puzzle_list}")
          # TODO: show the puzzle
          # TODO: change print statement to say "Yes, there is/are X {letter}(s)"
          # TODO: subtract 200 points from player's total points
        else:
          print(f"I'm sorry, there are no {letter}s.")
      else: 
        print(f"I'm sorry. {letter} is not a vowel.")

    elif int(player_choice) == 3:
      puzzle_attempt = input("What is the puzzle?\n")
      if puzzle_attempt.upper() == puzzle.upper():
        print(f"Congratulations {players[0]}! You solved the puzzle!")
        game_over = True
      else:
        print(f"I'm sorry, {players[0]}, that is incorrect. {players[1]}, it is your turn.")

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




