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
    
    def __repr__(self) -> str:
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)
    def __str__(self) -> str:
        return "{} - {}".format(self.fullname(),self.email)
    def __add__(self,other):
        return self.pay + other.pay

emp_1 = Employee("ahmed","Benjelloun",5000)
emp_2 = Employee("hamid","benny",6000)

print(emp_1)

print(emp_1 + emp_2)
