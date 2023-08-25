class Fraction:
    def __init__(self,s,m):
        self.s = s
        self.m = m
    def show(self):
        print(self.s ,"/" , self.m)
    def mul(self ,f):
        result = Fraction(None,None)
        result.s = self.s * f.s
        result.m = self.m * f.m
    def sum(self,f):
        result = Fraction(None , None)
        result.s = self.s * f.m + self.m * f.s
        result.m = self.m * f.m 
    def division(self,f):
        result = Fraction(None,None)
        result.s = self.s * f.m 
        result.m = self.m * f.s
    def sub(self,f):
        result = Fraction(None,None)
        result.s = self.s * f.m - self.m * f.s
        result.m = self.m * f.m 
        
        
f1 = Fraction(3,5)
f2 = Fraction(4,5)
f1.show()
f2.show()
result_m = f1.mul(f2)
result_m.show()
result_s = f1.sum(f2)
result_s.show()
result_d =f1.division(f2)
result_d.show()
result_s1 = f1.sub(f2)
result_s1.show()