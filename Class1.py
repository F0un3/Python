class members:
    
    raise_ammount = 1.04
    num_of_mem = 0

    # Takes the first, last, and pay and assignes it everytime the class is called
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        # This is a class variable
        # The num_of_mem will increase by 1 every time the class is called on an object
        members.num_of_mem += 1
    # print(members.num_of_mem)
    
    # After given the full name calling this will return the full name
    # This is a method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_ammount)

#mem1 and mem2 are objects of the class members
# Assign both members with names and pay
mem1 = members("John", "Smith", 50000)
mem2 = members("Amy", "Williams", 60000)

print(members.num_of_mem)

# mem1.raise_ammount = 1.05

# # print(mem1.__dict__)

# print(members.raise_ammount)
# print(mem1.raise_ammount)
# print(mem2.raise_ammount)