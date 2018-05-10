
class Employee:

    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print('Total Employee %d' % Employee.empCount)

    def displayEmployee(self):
        print('Name: ', self.name, ', Salary: ', self.salary)

class Test:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)

# t = Test()
# t.prt()

emp1 = Employee('zara',2000)
emp2 = Employee('manni',5000)

emp1.displayEmployee()
emp2.displayEmployee()
print('Total Employee %d' % Employee.empCount)

emp1.age = 7
print(emp1.age)
emp1.age = 8
print(emp1.age)
#del emp1.age
# print(emp1.age)
print(hasattr(emp1, 'age'))    # 如果存在 'age' 属性返回 True。
print(getattr(emp1, 'age') )    # 返回 'age' 属性的值
print(setattr(emp1, 'age', 8))  # 添加属性 'age' 值为 8
print(delattr(emp1, 'age') )    # 删除属性 'age'