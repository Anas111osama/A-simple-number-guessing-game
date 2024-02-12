
import random
import time
file=open(r"C:\Users\Anas\Desktop\Number-Guessing-game-main\L-B.txt","a")
name =str(input("Enter your name:"))
points=0
try1=15
num=0
num+=1
# print(help(random.randint))




class users():
   def __init__(self,name,points,level) :
      self.name = name
      self.points = points

users.name=name
users.points = points
re=True

while True:
 print(f"Hi {name.capitalize().strip()}")
 print("There are three levels in the game ")
 print("level one => ones number")
 print("level two => tens number")
 print("level Three => Hundreds number")
 level = int(input("Choose a level \n For level one enter 1 \n For level two enter 2 \n For level three enter 3 \n Enter the level:"))
 if level == 1:
    print("Let`s start level one")
    for num in range (try1):
     number = random.randint(0,10)
     if number < 5:
         print("Hint: The number is smaller than 5")
     elif number >= 5:
         print("Hint: The number is bigger than or equal 5")
     if number%2==0:
         print("Hint: Number is even")
     elif number%2==1:
         print("Hint: Number is odd")
     n1 = int(input("Enter your guess"))
     if n1==number:
         points +=1
         print("Good"or"Very good")
     elif n1==number:
         points-=1
         print("Try again")
    if points > 5:
        print (f"You win you have {points} points")
    else:
        print(f"You lose you have {points} points")
    try1=15
    
 elif level == 2:
    print("Let`s start level two")
    for num in range (try1):
     number = random.randint(10,100)
     if number < 50:
         print("Hint: The number is smaller than 50")
     elif number >= 50:
         print("Hint: The number is bigger than or equal 50")
     if number%2==0:
         print("Hint: Number is even")
     elif number%2==1:
         print("Hint: Number is odd")
     n1 = int(input("Enter your guess"))
     if n1==number:
         points +=1
         print("Good"or"Very good")
     elif n1==number:
         points-=1
         print("Try again")
    if points > 5:
        print (f"You win you have {points} points")
    else:
        print(f"You lose you have {points} points")
    try1=15
    print("Let`s start level two")
    for num in range (try1):
     number = random.randint(100,1000)
     if number < 500:
         print("Hint: The number is smaller than 500")
     elif number >= 50:
         print("Hint: The number is bigger than or equal 500")
     if number%2==0:
         print("Hint: Number is even")
     elif number%2==1:
         print("Hint: Number is odd")
     if number%4==0:
         print("Hint: Number is divisible by 4")
     if number%5==0:
         print("Hint: Number is divisible by 5")
     if number%8==0:
         print("Hint: Number is divisible by 8")
     if number%10==0:
         print("Hint: Number is divisible by 10")
     n1 = int(input("Enter your guess"))
     if n1==number:
         points +=1
         print("Good"or"Very good")
     elif n1==number:
         points-=1
         print("Try again")
    if points > 5:
        print (f"You win you have {points} points")
    else:
        print(f"You lose you have {points} points")
    try1=15
 play=input("Do you want to continue playing(y/n)")
 
 if play.lower()=="n"or play.lower=="no":
        break
 elif play.lower()=="y"or"yes" :
        re=True
 else:
        print("You enter a false input w will take you out of the game")
        break
    
file.write(f"User {num}: \n The Name: {name} \n Points = {points}")

