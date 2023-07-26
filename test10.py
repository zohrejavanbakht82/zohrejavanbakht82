import math
op = input("Enter a operator(* ,/ ,+ ,- ,sin ,cos ,tan , cot ,! ,**1/2) : ")
if op == "*" or op == "/" or op == "+" or op == "-":
    A = int(input("Enter a number: "))
    B = int(input("Enter a number: "))
    if op == "*" :
        print(A * B)
    elif op == "/" :
        if B == 0 :
            print("Erorr")
        else :
            print(A / B)
    elif op == "+":
        print(A + B)
    else :
        print(A - B)
elif op =="sin" or op == "cos" or op == "tan" or op == "cot" :
    C = int(input("Enter an angle in radian : "))
    if op == "sin":
        print(math.sin(C))
    elif op == "cos" :
        print(math.cos(C))
    elif op == "tan":
        print(math.tan(C))
    else :
        print(math.cot(C))
elif op == "!":
    D = int(input("Enter a number: "))
    n = 1 
    for i in range(1,D+1) :
        n*= i
    print(n)
else :
    E = int(input("Enter a number: "))
    print(math.sqrt(E))
    
    