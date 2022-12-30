import math
from GUI.Soldier import Soldier
import math


def binary_to_decimal(number):
    return int(number, 2)


def decimal_to_binary(number):
    return bin(number).replace("0b", "")


def highest_power_of_2(n):
    p = int(math.log(n, 2))
    return int(pow(2, p))


def main_circle(number, create_image, create_text, window_data: dict, man_image) -> Soldier:
    small_circle_r = 70 / math.sqrt(number)

    root = Soldier(data="root")
    current = root

    try:
        window_height = int(window_data["window_height"])
        window_width = int(window_data["window_width"])
    except:
        raise Exception("window_width and height should be integer.")

    circle_o_x = (window_width / 2)
    circle_o_y = (window_height / 2) - 15

    circle_r = 270  # 200 px
    # then the first element should be on (circle_o - circle_r) position
    chop_radian = (2 * math.pi) / number
    angle = 0
    for i in range(number):
        x = circle_o_x + circle_r * math.sin(angle)
        y = circle_o_y - circle_r * math.cos(angle)
        small_circle = create_image(x, y, image=man_image)
        if number < 30:
            text = create_text(x+1, y, text=i + 1, font=('courier', 15, 'bold'), fill="green")
        else:
            text = create_text(x + 1, y, text=i + 1, font=('courier', 1, 'bold'), fill="green")

        angle += chop_radian

        small_circle_data = {
            "data": small_circle,
            "number": text
        }
        newSoldier = Soldier(data=small_circle_data)
        current.after = newSoldier
        current = current.after

    root = root.after
    current = root
    while current.after:
        current = current.after

    current.after = root

    return root


