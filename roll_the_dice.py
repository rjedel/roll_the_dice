from random import randint


def multiply_points(text):
    return int(text[:text.index('D')]) if text.index('D') else 1


def dice_value(code):
    if '+' in code:
        return int(code[code.index('D') + 1:code.index('+')])
    elif '-' in code:
        return int(code[code.index('D') + 1:code.index('-')])
    return int(code[code.index('D') + 1:])


def change_result(sign):
    if '+' in sign:
        return int(sign[sign.index('+') + 1:])
    elif '-' in sign:
        return -int(sign[sign.index('-') + 1:])
    return 0


def throw_the_dice(dice_code):
    """Calculate dice roll from dice pattern.

    :param str dice_code: dice pattern ex. `7D12-5`
    :return: dice roll value for proper dice pattern, `Wrong dice code` text elsewhere
    """
    dice_code = dice_code.upper().strip()
    try:
        modifier = change_result(dice_code)
        dice_type = dice_value(dice_code)
        multiply = multiply_points(dice_code)
        return sum([randint(1, dice_type) for _ in range(multiply)]) + modifier
    except Exception:
        return 'Wrong dice code'


if __name__ == "__main__":
    print(throw_the_dice("2D10+10"))
    print(throw_the_dice("D6"))
    print(throw_the_dice("2D3"))
    print(throw_the_dice("D12-1"))
    print(throw_the_dice("DD34"))
    print(throw_the_dice("4-3D6"))
    

