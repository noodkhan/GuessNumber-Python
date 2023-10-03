import random 

def game():
    win = 0
    print("Welcome to Guessing Game") 
    print("__________________________")
    minimum = int(input("Please Enter Minimum Range => "))
    print("Your Minimum Range = " , minimum)
    print("__________________________")
    maxium = int(input("Please Enter Maxium Range =>  "))
    print("Your Maxium Range = " , maxium)
    print("__________________________")
    print("     You've Only Have 7 Chances To guess The Number          ")
    print("")
    num = random.randint(minimum , maxium)
    count = 7 
    while count != 0 : 
        UserInput = int(input("Please Enter Your Guess Number => "))
        count = count - 1
        if UserInput == num:
            print(" Number of Guess " , count)
            print(" Yes ! That is Number => num = " , num)
            win = 1
            break
        if UserInput > num :
            print(" No! It's Lower Than That ")
            print("Chances = " , count)
        else :
            print(" No! It's High Than That ") 
            print("Chances = " , count)

    if win == 0 : 
        for i in range(1 , 70):
             print("         Fcking Noob Lose !  Quit Plz!     ")
    else :
        for i in range(1 , 70):
            print("         You WIN TOO COOL 4 You !      ") 


game() 
for i in range(0 , 5):
    print("     ")
print("     Thanks For Playing The Game         ")
for i in range(0 , 5):
    print("     ")

re = str(input("        Do You Wish To Start A New Game ?           Y OR N          => " )) 
if re == "Y":
    game()

for i in range(0 , 5):
    print("Stop Playing !")