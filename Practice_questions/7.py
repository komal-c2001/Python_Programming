def calculate_salary(basic_salary, bonus=2000):
    Total_Salary = basic_salary + bonus
    return Total_Salary
print("Employee 1 Salary:",calculate_salary(29000,3000)) #Positional Arguments
print("Employee 2 Salary:",calculate_salary(basic_salary = 30000,bonus = 5000)) #Keyword Arguments
print("Employee 3 Salary:",calculate_salary(25000)) #Default Arguments