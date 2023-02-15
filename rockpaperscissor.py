from random import randint

list1 = ("rock", "paper", "scissors")

player = False

computer = list1[randint(0,2)]

print("Welcome to rock, paper or scissors.")
print()
print("Choose rock, paper, or scissors.")


while player == False:
    player = input("rock paper or scissors?")
    if list1 == computer:
        print("Tie")

if list1 == ("rock") and computer == ("scissor"):
    print("You won")