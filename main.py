from utils.utils import decimal_to_binary, binary_to_decimal


def survivor_number_binary(population):  # works for only k == 2
    pbf = decimal_to_binary(population)
    first_character = list(pbf)[0]
    survivor_binary = ""
    for i in range(len(pbf)):
        if i != 0:
            survivor_binary += pbf[i]
    survivor_binary += first_character
    return binary_to_decimal(survivor_binary)


def survivor_number_decimal(population):
    pass


print(survivor_number_binary(int(input("enter number of people: "))))
