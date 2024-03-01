#rock paper scissors
import random

choices = ["rock", "paper", "scissors"]
currentRound = 1
computerscore = 0
playerscore = 0
ties = 0
roundsToPlay = int(input("How many rounds do you want to play? "))
while roundsToPlay != currentRound:
  computer = random.choice(choices)
  player = "nothingpicked"
  print("ROUND", currentRound)
  
  while player not in choices:
    player = input("Rock, paper or scissors?: ").lower()
  
  if player == computer:
    print("computer: ", computer)
    print("player: ", player)
    print("Tie!")
    ties = ties + 1
    
  elif player == "rock":
      if computer == "paper":
        print("computer: ", computer)
        print("player: ", player)
        print("You lose!")
        computerscore = computerscore + 1
      if computer == "scissors":
        print("computer: ", computer)
        print("player: ", player)
        print("You win!")
        playerscore = playerscore + 1
  
  elif player == "paper":
    if computer == "rock":
      print("computer: ", computer)
      print("player: ", player)
      print("You win!")
      playerscore = playerscore + 1
    if computer == "scissors":
      print("computer: ", computer)
      print("player: ", player)
      print("You lose!")
      computerscore = computerscore + 1
  
  elif player == "scissors":
    if computer == "rock":
      print("computer: ", computer)
      print("player: ", player)
      print("You lose!")
      computerscore = computerscore + 1
    if computer == "paper":
      print("computer: ", computer)
      print("player: ", player)
      print("You win!")
      playerscore = playerscore + 1

  input("Hit ENTER to continue.")
  currentRound = currentRound + 1

print("")
print("FINAL SCORES: ")
print("COMPUTER: ", computerscore)
print("PLAYER: ", playerscore)
print("TIES: ", ties)

if computerscore > playerscore:
  print("YOU LOSE!")
elif playerscore > computerscore:
  print("YOU WIN!")
else:
  print("TIE!")
  