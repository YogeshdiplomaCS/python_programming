import random
while True:
    roll=random.randint(1,6)
    print(f" You rolled : {roll}")
    again=input("Roll again? (y/n)")
    cur=0
    tol=cur+roll
    tol1=tol+roll
    tol=tol1

    print(f" Total {tol1}")
    if again != "y":
        break
