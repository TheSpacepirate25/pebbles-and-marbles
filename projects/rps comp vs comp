#rock paper scissors
import random

choices = ["rock", "paper", "scissors"]
currentRound = 1
computer1score = 0
computer2score = 0
ties = 0
roundsToPlay = int(input("How many rounds do you want to play? "))
roundsToPlay = roundsToPlay + 1
while roundsToPlay != currentRound:
  computer1 = random.choice(choices)
  computer2 = random.choice(choices)
  print("ROUND", currentRound)
  
  if computer1 == computer2:
    print("computer1: ", computer1)
    print("computer2: ", computer2)
    print("Tie!")
    ties = ties + 1

  elif computer1 == "rock":
    if computer2 == "paper":
      print("computer1: ", computer1)
      print("computer2: ", computer2)
      print("Computer 2 wins!")
      computer2score = computer2score + 1
    if computer2 == "scissors":
      print("computer1: ", computer1)
      print("computer2: ", computer2)
      print("Computer 1 wins!")
      computer1score = computer1score + 1

  elif computer1 == "paper":
    if computer2 == "rock":
      print("computer: ", computer1)
      print("computer2: ", computer2)
      print("Computer 1 wins!")
      computer1score = computer1score + 1
    if computer2 == "scissors":
      print("computer1: ", computer1)
      print("computer2: ", computer2)
      print("Computer 2 wins!")
      computer2score = computer2score + 1

  elif computer1 == "scissors":
    if computer2 == "rock":
      print("computer1: ", computer1)
      print("computer2: ", computer2)
      print("Computer 2 wins!")
      computer2score = computer2score + 1
    if computer2 == "paper":
      print("computer1: ", computer1)
      print("computer2: ", computer2)
      print("Computer 1 wins!")
      computer1score = computer1score + 1

  currentRound = currentRound + 1

print("")
print("FINAL SCORES: ")
print("Computer 1: ", computer1score)
print("Computer 2: ", computer2score)
print("Ties: ", ties)

if computer1score > computer2score:
  print("Computer 1 wins!")
elif computer2score > computer1score:
  print("Computer 2 wins!")
else:
  print("TIE!")
