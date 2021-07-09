class Employee:
    def __init__(self,first,last,pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + last + '.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp_1 = Employee("ahmed","Benjelloun",5000)
emp_2 = Employee("hamid","benny",6000)

# emp_1.FirstName = "Slim"
# emp_1.LasName = "Hamedani"

print(emp_1)
print(emp_2.fullname())
print(Employee.fullname(emp_1))