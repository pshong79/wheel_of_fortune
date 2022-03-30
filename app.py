import random

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


player1 = input("Enter Player 1's name: ")
player2 = input("Enter Player 2's name: ")
player3 = input("Enter Player 3's name: ")

player1_score = 0
player2_score = 0
player3_score = 0

who_goes_first = random.choice([player1, player2, player3])
print(f"{who_goes_first} will go first")

player_options = f"""
Do you want to:
1. Spin
2. Buy a vowel
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
