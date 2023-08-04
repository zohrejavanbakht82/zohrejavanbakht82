import random
pc_number = random.randint(0,20)
count = 0
while True :
    count+=1
    user_number = int(input("enter the number you guess : "))
    if user_number == pc_number :
        print("Hora!!!")
        break
    elif user_number < pc_number :
        print("Bigger!!")
    elif user_number > pc_number :
        print("smaller!!")
print(count)