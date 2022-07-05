import random

def swg(comp,mine):
    if comp==mine:
        return None
    if comp== 's' and mine == 'g':
        return True
    elif comp== 'w'  and mine == 's':
        return True
    elif comp == 'g'and mine =='w':
        return True
    else:
        return False
n=int (input('enter the no of give u want to play : '))

while(n>0):
    t=0
    f=0
    choice=('s','w','g')
    comp=random.randint(0,2)
    comp=choice[comp]
    mine=input("enter your choice : s : w : g :->")
    win=swg(comp,mine)
    print(f" your choce is {mine} and the computer choice is {comp} ")
    if win is None:
        print("draw match")
        
    if win is True:
        print("you win")
        t=t+1
    if win is False:
        print("you lost")
        f=f+1
   
    n=n-1
if(f>t):
    print("you lost finally")
elif t>f:
    print("you won finally")
else:
    print("draw ho gaya")





