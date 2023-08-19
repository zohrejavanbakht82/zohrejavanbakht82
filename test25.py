text = input("Enter a text: ")
count = 1
for i in range(len(text)):
    if text[i] == " " :
        count +=1
print(count)
print("***************************")
lst = []
n = int(input("tedad aazai list : "))
for i in range(n) :
    item = int(input("Enter a number : "))
    lst.append(item)
print(lst)
lst.sort()
print(lst)