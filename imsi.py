#!/usr/bin/python3

class Employee:
    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first+"."+last+"@company.com"
        self.pay = pay

        Employee.num_of_emp += 1

    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.__dict__)
#print(emp_2)
#Manual assignment
#emp_1.first = "Corey"
#emp_1.last = "Schafer"
#emp_1.email = "Corey.Schafer@company.com"
#emp_1.pay = 50000

#emp_2.first = "Test"
#emp_2.las = "User"
#emp_2.email = "Test.User@company.com"
#emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(Employee.fullname(emp_1))

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1.raise_amount = 1.06
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_1.__dict__)
print(Employee.num_of_emp)
