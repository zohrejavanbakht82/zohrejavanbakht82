import random
n = int(input("Enter the length of the list:  "))
lst1 = list(range(0,100))
random.shuffle(lst1)
print(lst1[:n])