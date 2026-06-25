# BlackJack Card Game

BlackJack is a card game where there is a user and a dealer. Rules are as follows:
### Rules:
* Both dealer and user gets two cards initially, with one of the dealer cards being hidden.
* The user can 'hit' or 'stand' depending on their choice.
* If they 'hit' a card gets added.
* If the card sum exceeds 21, they lose.
* If they 'stand'  i.e. satisfied with their cards sum then dealer will get cards until the sum is greater than 17.
* The sum closer to 21 wins, else its draw. 

## Uniqueness:

- Traditional blackjack games are built for one player versus a dealer. Multiplayer system is more engaging than 1 vs 1 and is complex to build comparatively. 

- To make my project unique, I haver added multiplyer system where there is one dealer and multiple people according to the number of people entered. 

- I implemented a sequential turn system where each player independently decides to hit or stand. Then, results are compared individually against the dealer.

## Concepts Applied:

* **Function:** Functions are created to reuse the code. Also, inbuilt function like `sum()` has been applied.
* **Conditionals:** `if-else` statements are used repeatedly to check the conditions and if they match the rules.
* **Loops:** `while` loop is used to keep the game going and ask the user to either 'hit' or 'stand'.
* **List:** `list` have been used to keep track of cards of both the user and dealer. 
