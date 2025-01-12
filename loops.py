# n = 1
# while n<=100:
#     print(n)
#     n=n+1

# n = 1
# while n<=100:
#     print("hello",n)
#     n+=1


# n = 100
# while n>=1:
#     print(n)
#     n-=1


# n = int(input("Enter the number:"))
# i = 1 
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i+=1

# Q. print the elements of the following list using a loop:
# num = [1,4,9,16,25,36,49,64,81,100]

# idx = 0
# while idx<len(num):
#     print(num[idx])
#     idx+=1

# Q.  search for a number x in this tuple using loop:
num = (1,4,9,16,25,36,49,64,81,100)
x = 36
i = 0
while i<len(num):
    if (num[i]==x):

        print("Found at idx:",i)
    i+=1