import math
def degree2(a, b, c):
    DElts1 = (b*b) - 4*(a*c)
    if DElts1 == 0 :
        print("The equation has a root.")
        X = -b /(2*a)
        print(X)
    elif DElts1 < 0 :
        print("The equation not has a root.") 
    elif DElts1 > 0 :
        print("The equation has two root.")
        M = math.sqrt(DElts1)
        X1 = -b + M /(2 * a)
        X2 = -b - M /(2 * a)
        print(X1,X2) 
# Example :
degree2(1,-4,4)

           