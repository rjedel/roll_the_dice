from roll_the_dice import throw_the_dice


def points_throw(player_score, game_rnd, dice_code='2D6'):
    """Calculate score and shows the current random roll score.

    :param int player_score: current score
    :param int game_rnd: game round
    :param str dice_code: dice pattern, default: 2D6

    :rtype: tuple
    :return: new_score, last_roll
    """
    throw = throw_the_dice(dice_code)
    if game_rnd == 0:
        points = player_score + throw
    else:
        if throw == 7:
            points = player_score // 7
        elif throw == 11:
            points = player_score * 11
        else:
            points = player_score + throw
    return points, throw


def winner_is(player_1, player_2):
    if player_1 >= 2001 and player_2 >= 2001:
        return 'Draw!'
    elif player_1 >= 2001:
        return 'Player one wins!'
    elif player_2 >= 2001:
        return 'Computer wins!'


def dice_game_2001():
    """Main function of the program."""
    first_score = 0, 0
    second_score = 0, 0
    game_round = 0
    while first_score[0] < 2001 and second_score[0] < 2001:
        input('Press ENTER to roll the dices')
        first_score = points_throw(first_score[0], game_round)
        second_score = points_throw(second_score[0], game_round)
        game_round += 1
        print(f"Player one:\tthis rolls: {first_score[1]:<2} total points: {first_score[0]:<4}\n"
              f"Computer:\tthis rolls: {second_score[1]:<2} total points: {second_score[0]:<4}\n")
    print(winner_is(first_score[0], second_score[0]))


if __name__ == '__main__':
    dice_game_2001()
