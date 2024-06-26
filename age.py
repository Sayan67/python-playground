while(1):
    try:
        age = int(input("Enter the age : "))

        if age<13 and age>=0 :
            print("Child")
        elif age>=13 and age<20 :
            print("Teenager")
        elif age>=20 and age<60 :
            print("Adult")
        else:
            print("Senior Citizen")
        break
    except:
        print("Wrong input")