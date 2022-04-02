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

##### main program
consonants = [ 'B', 'C', 'D', 'F', 'G', 'H', 
               'J', 'K', 'L', 'M', 'N', 'P', 
               'Q', 'R', 'S', 'T', 'V', 'W', 
               'X', 'Y', 'Z'
             ]
vowels = [ 'A', 'E', 'I', 'O', 'U' ]

points = [ '100', '100', '100', '100', '100', '100',
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

puzzle = input("Enter a word or a phrase for the puzzle.\n")
puzzle_list = list(puzzle.upper())
print(puzzle_list)

# get a count of each letter in the puzzle_list
# 1. get length of list
# 2. iterate through list
# 3. while not at end of list, 
# 4. letter1.= item1
# 5. letter1_count = puzzle_list.count(letter1)
# 6. if item2 != item1
# 7. true -> letter2 = item2 and letter2_count = puzzle_list.count(letter2)
# 8. continue until end of list ()

players = []
players = define_player_order()

# TODO: need to assign flags to players to manage whose turn it is. 

while game_over == False:
  print(f"{players[0]}, would you like to:")
  player_options = f"""
1. Spin the wheel.
2. Buy a vowel.
3. Solve the puzzle.
"""
  player_choice = input(player_options)

  if int(player_choice) == 1:
    spin_points = random.choice(points)
    letter = input(f"For {spin_points}, which consonant would you like to choose?\n").upper()
  elif int(player_choice) == 2:
    letter = input(f"Which vowel would you like to choose?\n")
  else:
    print("Please select a valid option.")
    player_choice = input(player_options)

  # if # any letter matches:
  #   # show letters
  #   # add points
  #   # ask for options
  # else # no letters match
    # next person's turn




