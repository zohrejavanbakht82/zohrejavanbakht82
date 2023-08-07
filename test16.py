def shatrangee(a, b) :
    my_string = "* # "
    my_string1 = "# * "
    for i in range(b):
        for j in range(a) :
            if i % 2 == 0 :
                print(my_string[:a],end="")
            elif i %2 != 0 :
                print(my_string1[:a],end="")
        print()
#Example:
shatrangee(4,5)        
