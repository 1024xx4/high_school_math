# List 1-1 Convert from decimal to binary.
def dec2bin(target):
    amari = []  # List to put surplus.

    # Until the quotient of division becomes 0.
    while target != 0:
        amari.append(target % 2)  # Surplus.
        target = target // 2  # Quotient.

    # Returns the elements of the list in reverse order.
    amari.reverse()
    return amari


# List 1-2 Convert from decimal to hexadecimal.
def dec2hex(target):
    amari = []  # List to put surplus.

    # Until the quotient of division becomes 0.
    while target != 0:
        amari.append(target % 16)  # Surplus.
        target = target // 16  # Quotient.

    # Replace the surplus 10 to 15 with A to F.
    for i in range(len(amari)):
        if amari[i] == 10:
            amari[i] = 'A'
        elif amari[i] == 11:
            amari[i] = 'B'
        elif amari[i] == 12:
            amari[i] = 'C'
        elif amari[i] == 13:
            amari[i] = 'D'
        elif amari[i] == 14:
            amari[i] = 'E'
        elif amari[i] == 15:
            amari[i] = 'F'

    # Returns the elements of the list in reverse order.
    amari.reverse()
    return amari


# List 1-3 From m-ary to decimal.
def any2dec(target, m):
    n = len(target) - 1  # Maximum value of the index.
    sum = 0  # Value converted to decimal.

    # Repeat for the number of charactors.
    for i in range(len(target)):
        if target[i] == 'A':
            num = 10
        elif target[i] == 'B':
            num = 11
        elif target[i] == 'C':
            num = 12
        elif target[i] == 'D':
            num = 13
        elif target[i] == 'E':
            num = 14
        elif target[i] == 'F':
            num = 15
        else:
            num = int(target[i])

        sum += (m ** n) * num  # Sum "value of each row multiplied by n of m"
        n -= 1  # Reduce the weight by one.
    return sum
