# 1. 23----89 
# this number is between 23 to 89

# n =int(input("Enteer the number:"))
# if n>=23 and n<=89:
#     print("This number is between 23 to 89")
# else:
#     print("Invalid input")

# 2. user input this number 7 and 3 both valid not
# n =int(input("enter the number:"))
# if n%7==0 and n%3==0:
#     print("the number is divisible of both 3 AND 7")
# else:
#     print("plz input correct value--->>>>> ERROR")


# 3. user input this number 5 and 2 anyone valid 	not
# n = int (input("Enter the number:"))
# if n%2==0 and n%5==0:
#     print("Both number is divisible by 5 and 2")
# else:
#     print("Invalid input")

# 4. 
# user input 
# 1 :one 
# 2 :two 
# 3 :three
# 4 :four
# 5 :five 

# not match 

# n = int(input("Enter the number:"))
# if n==1:
#     print("one")
# elif n==2:
#     print("two")
# elif n==3:
#     print("three")
# else:
#     print("Not match")

# 5. week 7 : 

# 1 :sun
# 2:mon
# not match 
# ----------

# n = int(input("Enter the number:"))
# if n==1:
#     print("Sunday")
# elif n==2:
#     print("Monday")
# elif n==3:
#     print("Tuesday")

# else:
#     print("input mis match")


# #  by loop method:
# weekends= ["sunday","monday","tuesday","wednesday","thrusday","friday","saturday"]
# for i in weekends:
#     print(i)

# weekends= ["sunday","monday","tuesday","wednesday","thrusday","friday","saturday"]

# index = 0 
# while index<len(weekends):
#     print(weekends[index])
#     index = index+1


# 6. vowel and constonants
# n = input("Enter the any charcater:")
# if n=='a' or n=='e' or n =='i' or n=='o' or n=='u':
#     print("Vowels", n)
# else:
#     print("Consonant",n)


# 7. a :two number addition 

# s :subs

# m :multi

# d :divide

# o:modular 

# input mismatch 
# ------------- 

# n = (input("Enter any character:"))
# if n =='a':
#     print("This is addition programmm")
#     num1 = int(input("Enter the number :"))
#     num2 = int(input("Enter the number 2:"))
#     add = num1+num2

#     print("Addition of the program is :",add)
# elif(n == 's'):
#     print("This is a substraction programm")
#     num1 = int(input("Enter the number :"))
#     num2 = int(input("Enter the number 2:"))
#     sub = num1-num2
#     print("Substraction is ",sub)
# else:
#     print("Input mismatch")


# 8. s :swap without third variable 
# w :swap with third variable 

# input mismatch

# a = int(input("Enter the number:"))
# b = int(input("Enter the number:"))
# print(a)
# print(b)
# a ,b = b, a
# print("a",a)
# print("b",b)

# 9.swap with third variable
# a  = int(input("Enter 1:"))
# b = int(input("Enter 2:"))
# print(a) 
# print(b)
# c = a
# a= b
# b=c
# print("After swap:",a)
# print("After swap:",b)

# 10. celcius to fahrenhit convesion
# celcius  = float(input("Enter the temperature in celcius"))
# fahrenhite = (celcius*9/5)+32
# print(f"{celcius} celcius to {fahrenhite}")


# 11. C program to enter student marks and find percentage and grade
# A college has the following rules for the grading system:
# 5 marks (grade + %)
# 1. Below 25 – F
# 2. 25 to 45 – E
# 3. 45 to 50 – D
# 4. 50 to 60 – C
# 5. 60 to 80 – B 
# 6. Above 80 – A

# marks = int(input("enter the number:"))
# if marks<=25:
#     print("F")
# elif marks>=25 and marks<=45:
#     print("E")
# elif(marks>=45 and marks<=50):
#     print("D")
# elif(marks>=50 and marks<=60):
#     print("C")
# elif(marks>=60 and marks<=80):
#     print("B")
# elif(marks>=80):
#     print("A")
# else:
#     print("Invalid input")



# 12. three number maximum programm
# a = int(input("Enter the number1:"))
# b = int(input("Enter the number2:"))
# c = int(input("Enter the number3:"))
# number = [a,b,c]
# maximum = number[0]
# for i in number:
#     if i >maximum:
#         maximum = i

# print("The maximum number is :",maximum)


# 13.  number input 
# >40 
# average 
# 3. 45 to 50 – D
# 4. 50 to 60 – C
# 5. 60 to 80 – B
# 6. Above 80 – A 
# otherwise fail 

# marks = int(input("Enter the number:"))
# if marks<=40:
#     print("Fail")
# elif(marks>=45 and marks<=50):
#     print("D")
# elif(marks>=50 and marks<=60):
#     print("C")
# elif(marks>=60 and marks<=80):
#     print("B")
# elif(marks>=80):
#     print("A")
# else:
#     print("Invalid input")

# 14. five number maximum programm

# a = int(input("Enter the number 1:"))
# b = int(input("Enter the number 2:"))
# c = int(input("Enter the number 3:"))
# d = int(input("Enter the number 4:"))
# e = int(input("Enter the number 5:"))
# number = [a,b,c,d,e]
# maximum = number[0]
# for i in  number:
#     if i>maximum:
#         maximum = i
# print("The maximum number is :",maximum)



#  another method------>>>>>

# a = int(input("Enter the number 1:"))
# b = int(input("Enter the number 2 :"))
# c = int(input("Enter the number 3:"))
# d = int(input("Enter the number 4:"))
# e  = int(input("Enter the number 5:"))
# if a>b and a>c and a>d and a>e:
#     print("The maximum number is :",a)

# elif b>a and b>c and b>d and b>e:
#     print("The maximum number is :",b)
# elif c>a and c>b and c>d and c>e:
#     print("The maximum number is :",c)
# elif d>a and d>b and d>c and d>e:
#     print("The maximum number is :",d)
# elif e>a and e>b and e>c and e>d:
#     print("The maximum number is :",e)
# else:
#     print("Invalid input")

# 15. 5 number minimum programm

# 16. salalry :
# holidays (1) =full salary 
# 2-5 =5% 
# 5-14 =10% 
# 15 =50% 
# else =not salary 

# output : 
# name:
# address: 
# bank details: 
# salary : 
# alot :


# name = input("Enter employee's name: ")
# address = input("Enter employee's address: ")
# bank_details = input("Enter employee's bank details: ")
# base_salary = float(input("Enter employee's base salary: "))
# holidays = int(input("Enter number of holidays taken: "))

# if holidays == 1:
#     salary = base_salary
#     alot = "Full salary"
# elif 2 <= holidays <= 5:
#     salary = base_salary * 0.95
#     alot = "5% deducted"
#     print("5% deduction", base_salary * 5 / 100)
# elif 6 <= holidays <= 14:
#     salary = base_salary * 0.90
#     alot = "10% deducted"
# elif holidays == 15:
#     salary = base_salary * 0.50
#     alot = "50% deducted"
# else:
#     salary = 0
#     alot = "No salary"

# print("\nOutput:")
# print(f"Name: {name}")
# print(f"Address: {address}")
# print(f"Bank Details: {bank_details}")
# print(f"Salary: {salary}")
# print(f"Alot: {alot}")


