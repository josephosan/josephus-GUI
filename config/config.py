background_color = "#4B4453"
input_bg_color = "#B0A8B9"
text_color = "#00896F"


def killing_speed(number):
    return 5 / number


def man_size(number) -> int:
    if number < 7:
        return int(500/number)
    return int(1200 / number)


def killed_size(number) -> int:
    if number < 7:
        return int(300/number)
    return int(900 / number)
