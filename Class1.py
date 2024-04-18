class members:
    
    # Takes the first, last, and pay and assignes it everytime the class is called
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    # After given the full name calling this will return the full name
    # This is a method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

#mem1 and mem2 are objects of the class members
# Assign both members with names and pay
mem1 = members("John", "Smith", 50000)
mem2 = members("Amy", "Williams", 60000)

# print(mem1)
# print(mem2)

#to access the class members, we use the dot operator
# print(mem1.first)
# print(mem2.last)

#This does the same as the other code below just using the class name
print(members.fullname(mem1))
print(members.fullname(mem2))


# print(mem1.fullname())
# print(mem2.fullname())