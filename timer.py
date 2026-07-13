import time
secs=int(input("Enter the number of seconds: "))
while secs > 0:
    print(f"{secs} seconds remaining !")
    time.sleep(1)
    secs -= 1
print("Time's up!")
