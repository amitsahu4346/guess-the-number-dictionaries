import utility
import random
utility.draw_logo()

player_count = int(input("Enter No. of Players:"))
utility.clear_screen()

the_number = random.randint(1,100)
name_score = {}
winner = ''
difference = 100
for player in range (0,player_count):
    print(f"-----------Player {player+1}----------")
    name = input("Enter your Name:")
    u_number = int(input("Enter Number (1,100):"))
    diff = abs(the_number - u_number)
    if diff < difference:
        difference = diff
        winner = name
    utility.clear_screen()
    
print(winner, "Won the Match")        

