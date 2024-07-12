'''
User Input: Prompt the user to choose rock, paper, or scissors.
Computer Selection: Generate a random choice (rock, paper, or scissors) for
the computer.
Game Logic: Determine the winner based on the user's choice and the
computer's choice.
Rock beats scissors, scissors beat paper, and paper beats rock.
Display Result: Show the user's choice and the computer's choice.
Display the result, whether the user wins, loses, or it's a tie.
Score Tracking (Optional): Keep track of the user's and computer's scores for
multiple rounds.
Play Again: Ask the user if they want to play another round.
User Interface: Design a user-friendly interface with clear instructions and
feedback.
'''

import random
Result=[["Match Draw","You Win","You loose"],["You loose","Match Draw","You Win"],["You Win","You loose","Match Draw"]]
print("Rock, Paper, Scissor")
usrin = input("Enter your choice:")
if(usrin[0]=='R' or usrin[0]=='r'):
    usr=0
if(usrin[0]=='P' or usrin[0]=='p'):
    usr=1
if(usrin[0]=='S' or usrin[0]=='s'):
    usr=2

ls = ["Rock","Paper","Scissor"]
print(f"You have selected {ls[usr]}")
comp = random.randint(0,2)
print(f"Computer has selected {ls[comp]}")

print(Result[comp][usr])