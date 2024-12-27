# 1. Write a python program to print hello python.
# print("hello Python")

# 2. Write a python program to perform airthmetical operations.
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second Number:"))
# c = a+b
# d = a-b
# e = a*b
# f= a/b
# print("Additions of two numbers is : ",c)
# print("substraction of two number is :",d)
# print("Multiplications of two number is :",e)
# print("Division of two number is : " , f)

# 3 . Write a python program to find the area of triangle.
# a = float(input("Enter the first side of the triangle:"))
# b = float(input("Enter the second side of the triangle:"))
# c = .5*a*b
# print("Area of the triangle is:",c)

# 4. Write a python program to swap two variables.

# a= input("Enter the first variable:")
# b = input("enter the second vairable:")
# print(f"original value of a is {a} and b is {b}")
# c = a
# a = b
# b = c
# print(f"Swapped value of a is {a} and b is {b}")

# 5. Write a python program to generate a random number.
# import random
# print(f"Random number is : {random.randint(0,100)}")

# 6. Write a python program to convert kilometer to miles.

# kilometer = float(input("Enter the kilometer:"))
# miles = kilometer * 0.621371
# print(f"Kilometer is : {kilometer} and miles is : {miles}")

# 7. Write a python program to convert celsius to fahrenheit.
# celcius = float(input("enter the temperature in celcius :"))
# fahrenhiet = (celcius * 9/5) + 32
# print(f"Temperature i celcius is : {celcius} and in fahrenhiet is :{fahrenhiet}")

# 8. Write a python program to check if a number is positive,negative or zero.

# num = float(input("Enter the number:"))
# if num>0:
#     print(f"Number is {num} : Positive ")
# elif(num ==0):
#     print(f"Number is {num} : Zero")
# elif (num<0):
#     print(f"Number is {num} : Negative")
# else:
#     print("Invalid input ):")

# 9. Write a python program to check if a number is odd or even. 
# num = int(input("Enter the number:" ))
# if num%2==0:
#     print(f"Number is {num }: Even :)")
# elif num%2!=0:
#     print(f"Number is {num} : Odd ->:")
# else:
#     print("Input mismatched :(")

# 10. Write a python program to check leap year.
# year = int(input("Enter the Year :"))
# if year%4==0:
#     print(f" year is{year} : Leap Year")

# else:
#     print(f"year is {year } : Not a leap Year")

#      OR ------>>>>> with the help of the .format method string

# year = int(input("Enter the Year :"))
# if (year%400==0) and (year % 100==0):
#     print("{0} is a leap year".format(year))
# elif (year%4==0 ) and (year %100!=0):
#     print("{0} is a leap year ".format(year))

# else:
#     print("{0} is not a leap year".format(year))

# 11. Write a python program to check prime number.
# num  = int(input("Enter the number:"))
# if num ==1:
#     print(f"Number is  {num} : Not a Prime Number")
# if num >1:
#     for i in range(2,num):
#         if(num%i==0):
#             print(f"Number is {num} : not a prime Number")
#             break
#     else:
#         print(f"number is {num} : Prime Number")

# 12. Write a python program to print all prime number in an interval.
# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))
# for num in range(num1,num2+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break

#         else:
#             print(num)

# 13. Write a python program to find the factorial of a number.
# num = int(input("Enter the number:"))
# factorial =1
# if num<0:
#     print("Factorial does not exist for negative number")
# elif num==0:
#     print("Factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial = factorial*i
#     print(f"Factorial of {num} is {factorial}")
        
