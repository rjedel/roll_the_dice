from roll_the_dice import throw_the_dice
from random import randint

POSSIBLE_DICES = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']

POSSIBLE_DICES_DICT = {}
for key, value in zip([str(i) for i in range(1, (len(POSSIBLE_DICES) + 1))], POSSIBLE_DICES):
    POSSIBLE_DICES_DICT[key] = value


def calculate_points(player_score, current_score, game_rnd):
    """Calculate new score.

    :param int player_score: total score
    :param int current_score: points scored in a given dice roll
    :param int game_rnd: game round

    :rtype: int
    :return: new_total_score
    """
    if game_rnd == 0:
        points = current_score
    else:
        if current_score == 7:
            points = player_score // 7
        elif current_score == 11:
            points = player_score * 11
        else:
            points = player_score + current_score
    return points


def winner_is(player_1, player_2):
    if player_1 >= 2001 and player_2 >= 2001:
        return 'Draw!'
    elif player_1 >= 2001:
        return 'Player one wins!'
    elif player_2 >= 2001:
        return 'Computer wins!'


def dice_game_2001():
    """Main function of the program."""
    first_score = 0
    second_score = 0
    game_round = 0
    while first_score < 2001 and second_score < 2001:
        print('Dice to choose:\n' + ', '.join([(" - ".join(i)) for i in POSSIBLE_DICES_DICT.items()]))

        try:
            select_dice_first_1 = input('Select the dice for the first roll, e.g. enter 5 for D10\n'
                                        'Or press ENTER to roll D6 dice ')
            if not select_dice_first_1:
                select_dice_first_1 = '3'
            if select_dice_first_1 not in POSSIBLE_DICES_DICT:
                raise KeyError

            select_dice_first_2 = input('Select the dice for the second roll, e.g. enter 5 for D10\n'
                                        'Or press ENTER to roll D6 dice ')
            if not select_dice_first_2:
                select_dice_first_2 = '3'
            if select_dice_first_2 not in POSSIBLE_DICES_DICT:
                raise KeyError
        except KeyError:
            print('Enter a NUMBER that matches the dice from 1 to 8, e.g. "8"\n')
            continue

        select_dice_second_1 = str(randint(1, len(POSSIBLE_DICES_DICT))) if randint(1, 2) == 1 else '3'
        select_dice_second_2 = str(randint(1, len(POSSIBLE_DICES_DICT))) if randint(1, 2) == 1 else '3'

        first_roll_1 = throw_the_dice(POSSIBLE_DICES_DICT[select_dice_first_1])
        first_roll_2 = throw_the_dice(POSSIBLE_DICES_DICT[select_dice_first_2])

        first_sum = first_roll_1 + first_roll_2
        first_score = calculate_points(first_score, first_sum, game_round)

        second_roll_1 = throw_the_dice(POSSIBLE_DICES_DICT[select_dice_second_1])

        second_roll_2 = throw_the_dice(POSSIBLE_DICES_DICT[select_dice_second_2])

        second_sum = second_roll_1 + second_roll_2
        second_score = calculate_points(second_score, second_sum, game_round)

        game_round += 1

        print('Player one first roll => dice: {}, drawn: {}'.format(POSSIBLE_DICES_DICT[select_dice_first_1],
                                                                    first_roll_1))
        print('Player one second roll => dice: {}, drawn: {}'.format(POSSIBLE_DICES_DICT[select_dice_first_2],
                                                                     first_roll_2))
        print('Computer first roll => dice: {}, drawn: {}'.format(POSSIBLE_DICES_DICT[select_dice_second_1],
                                                                  second_roll_1))
        print('Computer second roll => dice: {}, drawn: {}'.format(POSSIBLE_DICES_DICT[select_dice_second_2],
                                                                   second_roll_2))
        print(f"Player one:\tthis rolls: {first_sum:<3} total points: {first_score:<4}\n"
              f"Computer:\tthis rolls: {second_sum:<3} total points: {second_score:<4}\n")
    print(winner_is(first_score, second_score))


if __name__ == '__main__':
    dice_game_2001()

