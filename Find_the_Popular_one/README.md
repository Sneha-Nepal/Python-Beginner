# Most Popular One
The Most_Popular_One is a guessing game where there is a user who guesses the most popular celebrity. Rules are as follows:

### Rules:
* The computer randomly generates two people from the dataset.
* The user can choose 'yes' or 'no' depending on who they think has more followers.
* If they guess correctly, their score increases and the game continues.
* The winner of the previous round becomes person to compare against a new contender.
* If the guess is wrong, they lose and it is Game Over.

## Concepts Applied:

**Import:** `import` has been used to get access to the `random` library of python and to get the data dictionary from another python file.

**Function:** `Functions` are created to reuse the code, such as comparing the data and validating the user's choices.

**Conditionals:** `if-else` statements are used repeatedly to check user input and determine the celebrity with the highest follower count.

**Loops:** `while` loop is used to keep the game going, track the high score, and ensure that the two randomly picked contenders are never the same.

**Data Structures:** `dictionary` has been used to look up and compare the entities' details, like names and follower counts, while `list` has been used to hold the overall dataset.
