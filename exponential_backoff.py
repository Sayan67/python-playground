import time
for i in range(1,5):
    otp = int(input("Enter otp : "))
    if otp != 0000:
        print("Wrong otp!!!\n Retry in :", 2*i, "seconds")
        time.sleep(2*i)
    else:
        print("login successful")
        break
