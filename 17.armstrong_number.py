# Armstrong NUmber: --> it is a number that is equal to the sum of cubes of its digits.
# 153 = 1^3 + 5^3 + 3^3 = 153
# Input from user
num = int(input("Enter a number: "))

# Calculate the sum of the power of each digit
sum_of_powers = 0
temp = num
num_digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp //= 10

# Check if the number is an Armstrong number
if num == sum_of_powers:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
