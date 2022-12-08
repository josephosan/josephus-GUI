import math


def binary_to_decimal(number):
    return int(number, 2)


def decimal_to_binary(number):
    return bin(number).replace("0b", "")


def highest_power_of_2(n):
    p = int(math.log(n, 2))
    return int(pow(2, p))
