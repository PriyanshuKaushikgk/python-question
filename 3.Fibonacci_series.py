# 15. Write a python program to print the Fibonacci series.
n = int(input("Enter the number of terms: "))

a, b = 0, 1

print("Fibonacci Series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
