class Time:
    def __init__(self,s,m,h) :
        self.s = s
        self.m = m
        self.h =  h
    def show(self,f):
        print(f"{f.h} : {f.m} : {f.s} ")
    def to_s(self,f):
        result = (((f.h * 60 ) + f.m ) * 60  ) + f.s 
            
        
t1 = Time(23,45,2)
t1.show()
result = t1.to_s()
     