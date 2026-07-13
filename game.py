import random
choices=["Rock", "Paper", "Scissor"]
user=input("Enter your choice: ")
cpu=random.choice(choices)
print("Cpu :",cpu)
if user == cpu:
    print("You win!")
