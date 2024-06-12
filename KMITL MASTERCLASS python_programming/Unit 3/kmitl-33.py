class Box:
    def get_area(self,w,l):
        return w*l
    def get_volume(self,w,l,h):
        return w*l*h
    
A = Box()
x = int(input("Input the width of your box: "))
y = int(input("Input the length of your box:"))
print("Box A has an area of =", A.get_area(x,y))

