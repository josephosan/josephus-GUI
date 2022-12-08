from utils.utils import decimal_to_binary, binary_to_decimal, highest_power_of_2


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
    closest_power_of_two = highest_power_of_2(population)
    l = population - closest_power_of_two

    surviving_position = (2 * l) + 1
    return surviving_position

