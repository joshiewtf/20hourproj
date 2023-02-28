# Mines
* [Running the console game module](#Running-the-console-game-module)
* [GUI version of Mines](#GUI-version-of-Mines)


## Running the console game module
1. Visit the project directory in your terminal / console
2. Type the following command into the console:
    * `python3 game.py`
3. A console version of the mines game will begin
4. Game instructions:
    * Type 'L' or 'R' to 'Left-click' or 'Right-click' respectively
    * Follow 'L' or 'R' with the coordinates which you would like to click
    * The first coordinate is horizontal distance starting from the left column (0)
    * The second coordinate is vertical distance starting from the top row (0)
        * ex: "L 0 0" or "R 2 2" or "L 12 9"
    * Flag all of the mines on the grid or reveal all safe spaces to win


## GUI version of Mines
1. Visit the project directory in your terminal /  console
2. Type the following command into the console:
    * `python3 run.py`
3. A gui version of the mines game will begin
4. The rules of the game are the same as other versions of the game above
5. Press 'Auto-Solve' at any point to have the AI solve the board

![GIF of the Mines GUI](images/hybrid-solve.gif)

**Note**: Please ensure you are using Python3.6 or greater and have pygame1.9.6 or greater installed
