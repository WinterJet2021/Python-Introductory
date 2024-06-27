class Box:
    def get_area(self,w,l):
        return w*l
box_A = Box()
box_B = Box()

print("box_A =", box_A.get_area(2,4))
print("box_B =", box_B.get_area(4,6))