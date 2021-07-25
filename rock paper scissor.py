import random
#  rock r paper p scissor s 
def gameWin(comp , you):

    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False     

    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True

    elif comp == 's':
        if you == 'r':
            return False
        elif you == 'p':
            return True 

print("Computer's turn Rock(r) Paper(p) Scissor(s)")                
randNum = random.randint(1,3)
if randNum == 1:
    comp = 'r'
elif randNum == 2:
    comp = 'p'
elif randNum == 3:
    comp = 's'

you = input("Your's turn Rock(r) Paper(p) Scissor(s) ?  ")                
b = gameWin(comp ,you)

print(f"the computer chose is {comp}")
print(f"the Yours chose is {you}")


if b == None:
    print("The Game is tied")
elif b:
    print("you won the Game")    
else :
    print("you Lose the Game")



