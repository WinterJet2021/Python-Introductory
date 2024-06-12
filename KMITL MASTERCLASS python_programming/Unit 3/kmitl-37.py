class Box:
    def __init__(self,name,w,l):
        self.name = name
        self.w = w
        self.l = l
    def get_area(self):
        return(self.w*self.l)
    def __str__(self):
        return(str(self.name)) + "has an area " + str(self.get_area())
    
box1 = Box("box_A ", 2,3)
box2 = Box("box_B ", 3,4)

A = [box1,box2]
print(A[0].get_area)
print(A[1].get_area)
print(A[0])
