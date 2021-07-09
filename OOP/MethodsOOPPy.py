import datetime

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
    
    @classmethod
    def set_raise_amnt(cls,amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
    
    @staticmethod
    def isit_work_day(day):
        if day.weekday() in (5,6):
            return True
        else:
            return False
        


emp_1 = Employee("ahmed","Benjelloun",5000)
emp_2 = Employee("hamid","benny",6000)

Employee.set_raise_amnt(1.09)

emp_1.apply_raise()
emp_2.apply_raise()
print(emp_1.pay)
print(emp_2.pay)

#from string

emp_str_1 = "zimmy-xxx-9000"
Employee.from_string(emp_str_1)

#work day

mydate = datetime.date(2016,7,10)
print(Employee.isit_work_day(mydate))

