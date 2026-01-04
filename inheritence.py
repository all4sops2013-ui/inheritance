lclass parent():
def __init__(self,id,name):
    self.id = id
    self.name = name
def display_Parent(self):
    print("The value of ID in parent class is:", self.id)

def display2_parent(self):
    print("This is a method to print the value of name", self.name)


class Child(Parent):
    def __init__(self,child_id,name):
        self.child = child_id
        self.name = name

    def display2_parent(self):
        return super().display2_parent()
    
    def display_Parent(self):
        return super().display_Parent()


ob_P = Parent('id1', P1)
ob_P.display2_parent()
ob_C = Child('c1','cname')
ob_C.display2_parent()



#task1

class Vehicle:

    def __init__(self,name,maximum_speed,mileage):
        self.name = name
        self.maximum_speed = maximum_speed
        self.mileage = mileage

    def display(self):
        print(self.name)
        print(self.maximum_speed)
        print(self.mileage)

class child_bus(Vehicle):
    pass

ob1 = child_bus("school volvo", 30, 25)
ob1.display()

    

        