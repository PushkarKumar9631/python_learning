##   INPUT STATEMENTS ##

# ## 1. RAW INPUT :-   Discontinued from python 3 upper versions
# x = raw_input("Enter First Number:") 
# print(type(x))    # It will always print  str type only for any input type

## 2. Input :-  input() function can be used to read data directly in our required format.We are not required to perform type casting.

# QUESTION:- Write a program to read 2 numbers from the keyboard and print sum.


a = int(input("Enter First Number"))
b = int(input("Enter Second Number"))

print(a+b)

# QUESTION:- Write a program to read Employee data from the keyboard and print that data.

eno=int(input("Enter Employee No:"))   
ename=input("Enter Employee Name:")   
esal=float(input("Enter Employee Salary:"))   
eaddr=input("Enter Employee Address:")   
married=bool(input("Employee Married ?[True|False]:"))   
print("Please Confirm Information")   
print("Employee No :",eno)   
print("Employee Name :",ename)   
print("Employee Salary :",esal)   
print("Employee Address :",eaddr)   
print("Employee Married ? :",married)  

