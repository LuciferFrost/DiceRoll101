import random

c=True
while c==True:
    dice=int(input("Number of sides in the dice"))
    x=random.randint(1,dice)
    print(x)
    check=input("Roll again?y/n")
    if check=="n":
        c=False
    elif check!="n":
        c=True
