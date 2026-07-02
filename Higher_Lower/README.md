# Higher-Lower Game

Higher-Lower is a classic guessing game where players try to find a hidden number within a range before running out of lives.

* The computer randomly generates a secret number within a specified range based on the current level.
* The player inputs a guess, and the game provides feedback on whether the actual number is "Too High" or "Too Low."
* The game continues until the player guesses correctly to progress or runs out of chances, resulting in a Game Over.

## Foundational Concepts:

* **Functions with Return Values:** Implemented `return` statements to safely pass success or failure signals from the local game function back to the main loop.
* **Variable Scope (Local vs. Global):** Managed local data like changing game states inside functions, while using the main loop to control global repetitive data like the current level.
* **Control Flow & Loops:** Used nested `while` loops to handle the core game rounds independently.
* **Conditional Statements:** Utilized structured `if-elif-else` conditionals to evaluate player guesses, adjust remaining lives, and dynamically set up level difficulty.

## Uniqueness:

To separate it from the standard tutorial designs, multi-stage **Level-Up System** is added. This features **three distinct levels** designed to challenge the users, where the number range expands and the available chances decrease with each level.
