# n = int(input("Enteer the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

n = int(input("Enter the number of rows:"))
k=1
for i in range(1,n+1):
    for j in range(1,k+1):
        print("*",end="")
    k+=2
    print()