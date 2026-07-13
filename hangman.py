import random
words=["python","coding","hangman"]
word=random.choice(words)
gussed=[]
attempts=6
while attempts > 0:
    display=[c if c in gussed else "_" for c in word]
    print(" ".join(display))
    g=input("Guess a word? ")
    if g not in word: attempts=attempts - 1
    else:
        gussed.append(g)
