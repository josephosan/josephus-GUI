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


def survivor_number_any_k(n, kth):
    soldiers = list(range(1, n + 1))

    k = 0
    survivedLastRound = n

    while survivedLastRound > 1:
        survived = 0

        for i in range(survivedLastRound):
            if i != k:
                soldiers[survived] = soldiers[i]
                survived += 1
            else:
                k += kth

        k -= survivedLastRound  # wrap around
        survivedLastRound = survived

    return soldiers[0]



