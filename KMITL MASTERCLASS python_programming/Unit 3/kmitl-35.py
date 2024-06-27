# Function to calculate area and volume of a box

class Box:
    def get_area(self,w,l):
        return w*l
    def get_volume(self,w,l,h):
        return w*l*h

box_A = Box()
box_B = Box()

print("box_A Area =", box_A.get_area(2,4))
print("box_A Volume =", box_A.get_volume(2,4,6))
print("box_B Area =", box_B.get_area(4,6))
print("box_B Volume=", box_B.get_volume(4,6,8))

