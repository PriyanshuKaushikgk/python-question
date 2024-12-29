# 16. Write a python Programm to find out the factorial number?
# n = int(input("Enter the number:"))
# fact = 1
# if n < 0 :
#     print("Factorial of 0 does not exist")
# if n==0:
#     print("Factorial of 0 is 1")
# if n>0:
#     for i in range(1,n+1):
#         fact = fact*i
# print("The factorial of given number is :",fact)



#              BY  RECURSION METHOD:----------->>>>>>

def fact(a):
    if a == 0:
        return 1
    else:
        return ((a)*fact(a-1))

num = int(input("Enter the number:"))
result = fact(num)
print("The given number factorial is :",result)