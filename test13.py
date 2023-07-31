import random
player = int(input("Enter a number (1 : play ,2 : exist) : "))
while True :
    if player == 1 :
        Test = random.randint(1,6)
        print(Test)
        if Test == 6 :
            for i in range(2):
                test = random.randint(1,6)
                print(test)
            break
        else :
            break
    elif player == 2 :
        print("Exist")
        break
    else :
        print("Error")    