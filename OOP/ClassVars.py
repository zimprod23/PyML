class Employee:
    raise_amount = 1.04
    num_of_emp = 0
    def __init__(self,first,last,pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + last + '.com'
        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def employee_num():
        return 'The number of employees is : {}'.format(Employee.num_of_emp)


emp_1 = Employee("ahmed","Benjelloun",5000)
emp_2 = Employee("hamid","benny",6000)

emp_1.raise_amount = 1.05
#Employee.raise_amount = 1.06 #Raise for all intances
emp_1.apply_raise()
emp_2.apply_raise()
print(emp_1.pay)
print(emp_2.pay)
#print(Employee.__dict__)

