number=int(input("Enter a number:"))
reversed_number=0

while True:
    last_digit=number % 10
    reversed_number=reversed_number*10 + last_digit
    number //= 10  # Use floor division to ensure number remains an integer

    if number <= 0:
        break

print(f"Reversed number:{int(reversed_number)}")