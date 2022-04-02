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
  player1_turn = False
  player2_turn = False
  player3_turn = False

  player_options = f"""
  1. Spin the wheel.
  2. Buy a vowel.
  3. Solve the puzzle.
  """

  players = []
  letters_of_puzzle = []

  # puzzle = input("Enter a word or a phrase for the puzzle.\n")
  puzzle = random.choice(possible_puzzles)
  puzzle_list = list(puzzle.upper())
  print(puzzle_list)
  letters_of_puzzle = get_all_letters_of_puzzle(puzzle_list)
  print(letters_of_puzzle)
  
  letter_count = count_number_of_letter_occurrance(puzzle_list, letters_of_puzzle)
  print(letter_count)


  # get a count of each letter in the puzzle_list
  # 1. get length of list
  # 2. iterate through list
  # 3. while not at end of list, 
  # 4. letter1.= item1
  # 5. letter1_count = puzzle_list.count(letter1)
  # 6. if item2 != item1
  # 7. true -> letter2 = item2 and letter2_count = puzzle_list.count(letter2)
  # 8. continue until end of list ()

  players = define_player_order()

  # TODO: need to assign flags to players to manage whose turn it is. 

  while game_over == False:
    print(f"{players[0]}, would you like to:")
    player_choice = input(player_options)

    if int(player_choice) == 1:
      spin_points = random.choice(points)
      letter = input(f"For {spin_points} points, which consonant would you like to choose?\n").upper()

      if letter in consonants:
        if letter in puzzle_list:
          print(f"{letter} is in the puzzle.")
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
        if letter in puzzle_list:
          print(f"{letter} is in the puzzle.")
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




