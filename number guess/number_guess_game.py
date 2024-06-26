import random

difficulty_level = input("Enter the the number of digit you want to play for(example: 4 digit -> 1000): ")

if(difficulty_level.isdigit()!=True):
    print("Wrong input.")
else:
    difficulty_level=int(difficulty_level)
    actual_number = random.randrange(1, (10 ** difficulty_level )- 1)
    i=0
    if(difficulty_level>=3):
        i = difficulty_level ** 2
    else:
        i=difficulty_level**3
    count=0

    while(i>0):
        print("You have "+str(i)+" chances.")
        guess=int(input("Guess the number : "))
        if guess==actual_number:
            print("Booyahh! you guessed it correct!")
            break
        elif(guess>actual_number):
            print("Go for a little lower.")
        else:
            print("Go for a little higher")
        i-=1

    print("Actual number was : "+str(actual_number))
    print("Your score is : 0" if (i<=0) else "Your score is : "+str(i))
