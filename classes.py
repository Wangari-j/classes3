class Employee:
    empName = "" 
    empAge = 0

empName1 = Employee()
empName2 = Employee()
empName3 = Employee()

empName1.empName = "Joy"
print(empName1.empName)

empName2.empName = "Lucy"
empName3.empName = "Ken"
print(empName2.empName)
print(empName3.empName)

empName1.empAge  = 30
empName2.empAge = 25
empName3.empAge = 27
print(empName1.empAge, empName2.empAge, empName3.empAge)


