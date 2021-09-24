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
