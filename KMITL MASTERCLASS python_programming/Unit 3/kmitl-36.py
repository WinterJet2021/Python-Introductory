# Function for area of box 1 and 2

class Box:
    def __init__    (self,w,l):
        self.w = w
        self.l = l
    def get_area(self):
        return(self.w*self.l)
    
box1 = Box(2,3)
box2 = Box(3,4)

A = [box1, box2]
print(A[0].get_area())
print(A[1].get_area())
