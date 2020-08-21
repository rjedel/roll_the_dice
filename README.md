# Dice pattern & Roll The Dice Game 2001

Many types of dice are used in board and paper RPG games, not only the well-known ones, 
cubic dice. One of the most popular dice is e.g. a 10-sided or even a hundred-sided dice!
Since dice are often rolled in games, writing each time e.g. _"roll two 10-sided dice,
and add 20"_ to the result, it would be boring, difficult, and waste a lot of paper.
In such situations, the code roll _"2D10+20"_ is used.

The code for such a dice looks like this:

##### xDy+z

where:
* __y__ &ndash; the type of dice to use (e.g. D6, D10),
* __x__ &ndash; number of dice rolls; if we throw once, this parameter is negligible,
* __z__ &ndash; a number to add (or subtract) to the result (optional).

__Examples:__

* __2D10+10__: 2 D10 rolls, add 10 to the result,
* __D6__: a simple roll of a cubic dice,
* __2D3__: a roll of two three-sided dice,
* __D12-1__: roll the D12 dice, subtract 1 from the result.


### roll_the_dice:

It is a module whose main function is a function _"throw_the_dice"_.
* this function accepts such a code in the form of a string in the parameter,
* it recognizes all inputs:
    * type of dice,
    * number of rolls,
    * modifier,
* if the given string is incorrect, it returns an appropriate message,
* performs a roll simulation and returns the result.

##### Roll The Dice Game 2001 &ndash; game rules:

Types of dice that are in the games: D3, D4, D6, D8, D10, D12, D20, D100.

1. Each player starts with a score of 0.
2. On its turn, the player rolls 2 dice (standard six-sided dice).
3. Rolled number of mesh is added to the total number of points.
4. Starting from the second round:
    * if the player rolls a 7, divides its points by that value, discarding the fractional part,
    * if 11 is rolled, the current number of points multiplied by the value,
5. The first player to score 2001 points wins.


### roll_the_dice_game_2001_v1:

* a game for two players.
* it is a console application.
* the second player is the computer.
* after each turn, the current number of points is displayed.
* the player's roll is performed after the player presses the enter.
The computer throw occurs automatically after the player's roll.
The program ends when the player or the computer reaches more than 2001 points.


### roll_the_dice_game_2001_v2:

Enhancements to the roll_the_dice_game_2001_v1:

* Before each roll, the player has a choice.
* The player can choose 2 dice from the set: D3, D4, D6, D8, D10, D12, D20, D100.
* Dice can repeat, and the player can use 2 different dice.
* The choice of the dice type is done by entering the appropriate number corresponding to the given type of dice:
1 - D3, 2 - D4, 3 - D6, 4 - D8, 5 - D10, 6 - D12, 7 - D20, 8 - D100 (one for each roll).
* The computer selects dice randomly.

The rest of the rules remain unchanged. 


### roll_the_dice_game_2001_v3:

Enhancements to the roll_the_dice_game_2001_v2. The game was transferred to the server using Flask framework.
The selection of the dice before the roll is done by the HTML form.


