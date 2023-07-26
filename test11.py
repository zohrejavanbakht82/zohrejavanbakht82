#triangle
A = float(input("Enter a side of the triangle: "))
B = float(input("Enter a side of the triangle: "))
C = float(input("Enter a side of the triangle: "))
if A < B + C :
    test = "there is a triangle."
else :
    test = "there is not a triangle."
if B < A + C :
    test =  "there is a triangle."
else : 
    test = "there is not a triangle."
if C < A + B :
    test = "there is a triangle."
else :
    test = "there is not a triangle."
print(test)
    
    