#armstrong number
no = int(input("Enter a number: "))
temp = no
sum = 0
order = len(str(no))

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if no == sum:
    print(no, "is an Armstrong number")
else:
    print(no, "is not an Armstrong number")
