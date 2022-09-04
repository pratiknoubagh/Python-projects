import random
def GameWin(comp,you):
    if(comp==you):
        return None
    elif(comp=="s"):
        if(you=="w"):
            return False
    elif(you=="g"):
        return True
    elif(comp=="g"):
        if(you=="s"):
            return False
    elif(you=="w"):
        return True
    elif(comp=="w"):
        if(you=="g"):
            return False
    elif(you=="s"):
        return True
print("Computer's Turn:Snake (s) Water(w) Gun(g)")
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'
yourturn=input("Your Turn:Snake(s)Water(w)Gun(g)")
a= GameWin(comp,yourturn)
print(f"Computer chose  {comp}")
print(f"You chose  {yourturn}")
if a==None:
    print("Game is tie")
elif a:
    print("You Win")
else:
    print("You Loose")

    