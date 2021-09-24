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