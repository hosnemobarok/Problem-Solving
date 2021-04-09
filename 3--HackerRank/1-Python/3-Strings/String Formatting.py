def print_formatted(n):
    space = len(bin(n)[2:])

    for i in range(1, n + 1):
        Decimal = str(i).rjust(space, " ")
        Octal = str(oct(i)[2:]).rjust(space, " ")
        Hexadecimal  = str(hex(i)[2:]).rjust(space, " ").upper()
        Binary = str(bin(i)[2:]).rjust(space, " ")

        print(Decimal, Octal, Hexadecimal, Binary)


