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

------
Diary


-- 21/02/2023 --
Hour 1, I designed the game itself using the console as a method of playing.
Hour 2, I made a tile system to simulate the different tiles within it.
Hour 2, I implemented a system to Left click or right click tiles using an input method. e.g. L 0 0 (left click) or R 0 0 (right click)
Hour 3, I started my base design of my ai that solves it within the console.
Hour 8, The AI was successfully trained over a course of 1000 games and was able to solve the game within a set amount moves.
-- 25/02/2023 --
Hour 12, I began my first design of the GUI. I reused my tile system and replaced the input system with a mouse click system.
Hour 14, The Gui was successfully built and the buttons were made to choose a size of the game.

-- 27/02/2023 --
Hour 17, I began my design of the AI for the GUI. I used the same AI as the console version but I had to change the way it was trained.
Hour 20, I successfully trained the AI over a course of 5461 games and was able to solve the game efficiently.



