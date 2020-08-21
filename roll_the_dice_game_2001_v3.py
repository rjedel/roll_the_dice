from flask import Flask
from flask import request
from roll_the_dice import throw_the_dice

from random import randint

app = Flask(__name__)

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
        return '<h1>Draw!</h1>'
    elif player_1 >= 2001:
        return '<h1>Player one wins!</h1>'
    elif player_2 >= 2001:
        return '<h1>Computer wins!</h1>'
    else:
        return 'No winners!'


def build_page(title, content):
    base = '''<!doctype html>
    <html lang="pl-PL">
    <head>
        <meta charset="UTF-8">  
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>{}</title>
    </head>
    <body>
        <h3>{}</h3>
        <hr>
        <div>
          {}
        </div>
    </body>
    </html>'''
    return base.format(title, title, content)


html_form = '<form method="POST"><span><b>Select the dice for first roll:</b></span><br>\n'
for key_, value_ in POSSIBLE_DICES_DICT.items():
    html_form += '<label><input type="radio" name="user_select_1" value="{}">{}</label>\n'. \
        format(key_, value_).replace('value="3"', 'value="3" checked')
html_form += '<br><br><span><b>Select the dice for second roll:</b></span><br>\n'
for key_, value_ in POSSIBLE_DICES_DICT.items():
    html_form += '<label><input type="radio" name="user_select_2" value="{}">{}</label>\n'. \
        format(key_, value_).replace('value="3"', 'value="3" checked')
html_form += '<input type="hidden" name="first_score_val" value="{}"><br>\n'
html_form += '<input type="hidden" name="second_score_val" value="{}"><br>\n'
html_form += '<input type="hidden" name="game_round_val" value="{}">\n'
html_form += '<input type="submit" value="Roll the dice"></form>'


@app.route("/", methods=['GET', 'POST'])
def try_to_guess():
    buff = ''
    if request.method == 'POST':
        """Main function of the program."""
        first_score = int(request.form['first_score_val'])
        second_score = int(request.form['second_score_val'])
        game_round = int(request.form['game_round_val'])

        select_dice_first_1 = request.form['user_select_1']
        select_dice_first_2 = request.form['user_select_2']

        first_roll_1 = throw_the_dice(POSSIBLE_DICES_DICT[select_dice_first_1])
        first_roll_2 = throw_the_dice(POSSIBLE_DICES_DICT[select_dice_first_2])

        first_sum = first_roll_1 + first_roll_2
        first_score = calculate_points(first_score, first_sum, game_round)

        select_dice_second_1 = str(randint(1, len(POSSIBLE_DICES_DICT))) if randint(1, 2) == 1 else '3'
        select_dice_second_2 = str(randint(1, len(POSSIBLE_DICES_DICT))) if randint(1, 2) == 1 else '3'

        second_roll_1 = throw_the_dice(POSSIBLE_DICES_DICT[select_dice_second_1])
        second_roll_2 = throw_the_dice(POSSIBLE_DICES_DICT[select_dice_second_2])

        second_sum = second_roll_1 + second_roll_2
        second_score = calculate_points(second_score, second_sum, game_round)

        game_round += 1

        text_1 = 'Player one first roll => dice: {}, drawn: {}'.format(POSSIBLE_DICES_DICT[select_dice_first_1],
                                                                       first_roll_1)
        text_2 = 'Player one second roll => dice: {}, drawn: {}'.format(POSSIBLE_DICES_DICT[select_dice_first_2],
                                                                        first_roll_2)
        text_3 = 'Computer first roll => dice: {}, drawn: {}'.format(POSSIBLE_DICES_DICT[select_dice_second_1],
                                                                     second_roll_1)
        text_4 = 'Computer second roll => dice: {}, drawn: {}'.format(POSSIBLE_DICES_DICT[select_dice_second_2],
                                                                      second_roll_2)
        text_5 = f"Player one: this rolls: {first_sum} total points: {first_score}"
        text_6 = f"Computer: this rolls: {second_sum} total points: {second_score}"

        text_7 = winner_is(first_score, second_score)

        if text_7 == 'No winners!':
            buff = html_form.format(
                first_score, second_score, game_round) + '<br>' + '\n<div>\n<p>' + '</p>\n<p>'.join(
                [text_1, text_2, text_3, text_4, text_5, text_6, text_7]) + '</p>\n</div>'
        else:
            buff = html_form.format(
                first_score, second_score, game_round).replace('<input type="submit" value="Roll the dice"></form>',
                                                               '</form>\n<p><b>Game over</b><p>') \
                   + '<br>' + '\n<div>\n<p>' + '</p>\n<p>'.join(
                [text_1, text_2, text_3, text_4, text_5, text_6, text_7]) + '</p>\n</div>'
    else:
        buff = html_form.format(0, 0, 0)

    return build_page("Roll the dice Game 2001", buff)


if __name__ == "__main__":
    app.run()

