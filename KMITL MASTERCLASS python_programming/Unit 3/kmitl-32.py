# Object oriented programming using python

# Class
"""
Rectangle
width
length
setWidth
setLength
getArea
"""

class Box:
    pass

a = Box()
b = Box()
print(a)
print(b)

"""class Box:
    def get_area(self, w, l):
        return w*l
    box_A = Box()
    box_B = Box()

    print("box_A =", box_A.get_area(2,4))
    print("box_B", box_B.get_area(4,6))"""

class Box:
    def get_area(self,w,l):
        return w*l
    def get_volume(self,w,l,h):
        return w*l*h
    
A = Box()
print("Box A = has an area of =", A.get_area(3,4))

