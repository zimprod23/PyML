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
        

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay,lang):
        super().__init__(first, last, pay)
        self.lang = lang


class Manager(Employee):
    def __init__(self, first, last, pay,Employee = None):
        super().__init__(first, last, pay)
        if Employee is None:
            self.employees = []
        else:
            self.employees = Employee
    
    def add_emp(self,new_emp):
        self.employees.append(new_emp)
    
    def remove_emp(self,target_emp):
        if target_emp in self.employees:
            self.employees.remove(target_emp)
    def print_emp(self):
        for emp in self.employees:
            print(emp.fullname())


#print(help(Developer))

dev_1 = Developer("ahmed","Benjelloun",5000,'java')
dev_2 = Developer("hamid","benny",6000,'c#')

manager_1 = Manager("ahmed","Benjelloun",5000,[dev_1,dev_2])


manager_1.print_emp()

print(isinstance(manager_1,Employee))



