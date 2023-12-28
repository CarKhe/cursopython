class A:
    def hablar(self):
        print("Hablar desde A")
class B(A):
    #def hablar(self):
        #print("Hablar desde B")
    pass
class C(A):
    def hablar(self):
        print("Hablar desde C")

class D(B,C):
    #def hablar(self):
    #   print("Hablar desde D")
    pass
        
d = D()
d.hablar()

print(D.mro())

C.hablar(d)