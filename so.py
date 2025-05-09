# Decimal to Binary using nested loops

def decimal_to_binary(num):
    binary = ""
    powers = []

    # Outer loop: find powers of 2 less than or equal to num
    power = 0
    while 2 ** power <= num:
        powers.append(2 ** power)
        power += 1

    # Reverse the powers for binary (start from highest power)
    powers = powers[::-1]

    # Nested loop to determine 1 or 0
    for i in range(len(powers)):
        bit = 0
        for _ in range(num // powers[i]):
            bit = 1  # Set bit to 1 if num >= current power
        binary += str(bit)
        if bit == 1:
            num -= powers[i]

    return binary

# Input from user
decimal = int(input("Enter a decimal number: "))
binary = decimal_to_binary(decimal)
print(f"Binary: {binary}")
