import random
randNum=random.randint(1,50)
guess=0
userGuess=None
while(randNum!=userGuess):
    userGuess=int(input("Enter the number:  "))
    guess+=1
    if(randNum==userGuess):
        print("You have guessed it right")
    elif(randNum<userGuess):
            print(" You guessed wrong Enter a smaller number")
    else:
            print("You guessed it wrong Enter a larger number")

print(f"You have made the guess in {guess} guesses")
with open("hiscore1.txt","r")as f:
    hiscore=int(f.read())
if(guess<hiscore):
    print("You have broken the hiscore")
    with open("hiscore1.txt","w") as f:
       f.write(str(guess))

