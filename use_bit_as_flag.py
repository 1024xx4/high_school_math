# 3.8 Use a bit as a flag.

# Flag initialization.
taro_item = 0

# Get gold coins.
taro_item = taro_item | 0b001  # Set a gold coin flag.
print(taro_item, bin(taro_item))

# Get a candy.
taro_item = taro_item | 0b1000  # Set a candy flag.
print(taro_item, bin(taro_item))

# Use the flag to detemine if you have candy.
chk_candy = taro_item & 0b1000
print(chk_candy, bin(chk_candy))

# Use a candy.
taro_item = taro_item & (~0b1000)  # Lower the candy flag.
print(taro_item, bin(taro_item))

# Use decimal numbers to manipulate flags.
taro_item = taro_item | 4  # Set a jewel flag.
print(taro_item, bin(taro_item))


def check_candy(item):
    if (item & 0b1000) != 0:  # Whether the candy flag set.
        print('持っている')
    else:
        print('持っていない')


taro_item = 9
check_candy(taro_item)
