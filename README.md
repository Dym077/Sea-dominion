# Sea-Dominion
![Sea Dominion](images/amiresponsive.png)

- Sea Dominion is a python-based battleships game which allows the player to battle against the computer in a classical battleships style. The player and the computer are both provided with a board on which the ships are randomly placed. The player will get 20 attempts to sink the computer's ships by guessing the position of the ships. The game is based both on luck and strategy, as the player has to guess the position of the computer's ships at first, while later being able to strategically pin down their position.

- The live link is found via this link - [Sea-Dominion](https://sea-dominion-cb02afeb3150.herokuapp.com/)


![Site Mockup](images/site-mockup.jpg)

## How to Play

### Gameplay
- When first opening the game the player will be presented with a menu, which explains the rules. The player will also be asked to enter a username, which has to be at least 4 characters long. It doesn't matter if the player uses lower or uppercase letters - the game will accept both.
After entering the username, the player will be greeted with the applied username and a line will declare: Begin sea battle!
- On the Gameboard, the player can see the ships, marked as "€". The purpose f the game is to find and sink all the computer's ships before the computer does the same with the player's ships. Having 20 attempts, the player must guess the position of the computer's ships by entering numbers representing horizontal and verical rows on the Gameboard.
When the player guesses a row on the board, the game will either say "{player}" HITS!" or "{player} MISSES!", depending on the outcome of the guess. A hit will display an "X", while a miss will display an "O". The player will then be informed how many attempts are left.

### Game over
- If the player manages to sink all the computer's ships the game will declare: "You won! All the computers ships have been sunk." If it's the other way around and the computer sinks the player's ships, the game will instead declare "You lost! All Your ships have been sunk." The player will then have the option to either quit the game or start a new game.
- Sometimes the game will result in a draw when all 20 attempts have been used. The game will then declare "Both players have ships remaining." The player will then have the option to either quit the game or start a new game.

### Exit game
- The player can choose to exit at any point during the game. when typing "exit", the game will declare that both player have ships remaining and the scores will be displayed. The player will then receive the question "Play another game? (yes/no): The player can choose either, and exactly as above in the 'Enter username' section, both lower and uppercase letters are accepted.

## Site Owner Goals
- To provide an easy-to-play, accessible game with rules that are easy to comprehend.
- That the player feels inspired to play the game by strategically guess the coordinates of the computer's ships.
- The player should feel that the game is challenging enough, but not too hard to play.
- The player should also feel that the game is an interactive experience.
- As a returning player, one should feel that one can upskill while learning the strategies of the game.

## User Stories

### First time user
- As a first time user, the player should be comfortable with the rules and terms of the game and should easily be able to start playing immediately.
- A first time user will also feel the interactivity of the game and access the game board easily.
- To a first time user, the game should be challenging without being confusing.

### Returning user
- A returning user should have no problem getting back into the rules of the game.
- A returning user can use and develop the strategies to more easily locate and sink the computer's ships.
- A returnign user should also be comfortable with playing multiple times to try to beat the computer.

### Frequent user
- The frequent user will develop the skills to beat the computer in a battleships game.
- The frequent user can enjoy the accessibility of the game's layout.
- As a frequent user You should also enjoy the challenge of the game's randomness. No round of the game will be exactly the same.

## Flow charts
When planning the logic flow of this game, I first started with pen and paper to get an idea of how the program should work.
![Flow Chart ](images/sea-dominion-first-flowchart.jpg)

- This was the first flowchart which later was replaced with the current one below. This one was created with Lucidchart snd provided a better overview of the flow of functions in the game. Even though it is a better presentation of how the game works, it doesn't cover the exact flow, as some of the functions were designed later. For example, the draw situationwith the declaration of "Both players have ships remaining", is not represented in the flowchart.

![Flow Chart](images/sea-dominion-flowchart.png)

## Design
- This game is based purely on python code and therefor it is totally text-driven. There are no graphic elements in the game - it runs in a terminal only. The plyer is prompted to use only the keyboard to execute the gameplay.

## Features
- When entering the site, the player will be greeted with a very basic text-based menu which explains the rules of the game. The player will be askesd to enter a username. The validation of the user input is strong - if the player enters anything but a four letter username, the game will throw an error message.
- After entering the username, the player will be presented with the game boards, with the player's board at the top and the computer's board at the bottom of the screen. The player's three ships will be visible as "€" on the board, while the computer's ships are hidden.
- The player will also be asked to guess the coordinates of the computer's ships. The player guesses these coordinates by typing numbers for each row and column on the board, e.g. "Enter row (0-4) : 2, Enter column(0-4) : 1". Also here, the validation of the user input is strong - if the player enters a word, a letter or a blank space instead of a number, the game will alert the player with "Interesting, but You should enter a number".
- The scores are updated instantly after each turn:
![Scores](images/turns-scores.png)

## Testing

### PEP8 Testing
- The code has been tested with the [Pep8 Online](https://pep8ci.herokuapp.com/#) validation tool, which currently returns these error/ warnings:

Results:
- 113: E501 line too long (86 > 79)
- 117: E303 too many blank lines (2)
- 125: E231 missing whitespace after ','
- 125: E501 line too long (95 > 79 characters)
- 159: E111 indentation is not a multiple of 4
- 159: E117 over-indented
- 194: E501 line too long (87 > 79 characters)
- 220: W292 no newline at end of file
* After correcting these errors, though, Gitpod will complain about them and the terminal will throw errors instead. The game works properly despite the errors that pep8 warns about.

### Input Testing
- The input validation has been tested to check that the rules for the correct input works properly.
Thorough playthrough with several input variations have been executed to ensure that the input validation works according to the flowchart.
- When the player is asked to type the username the screen should read:
![Enter username](images/enter-username.png)
- When done correctly, the screen will display this:
![Game boards](images/boards.png)
- When done incorrectly, the game will throw this error message:
![Invalid username](images/invalid-username.png)
- If the player enters anything but a number in the rows/columns- section under the board, the game adequately alerts the player with this message:
![Enter a number](images/interesting-but.png)
- When the player guesses a row and column right, the game correctly declares that it is a hit
The scores and turns that are left are also updated instantly:
![HIT](images/player-hits.png)
- If the player guesses a row and column wrong, the game adequately declares that it is a miss
The scores and turns that are left are also updated instantly:
![MISS](images/player-misses.png)
- When the game is over, the player will be asked "Play another game?". If the player types anything other than "yes" or "no", the game will throw this message correctly:
![Invalid](images/invalid-input.png)
- If the player types "yes", the games starts over gain with all values reset and two new boards.
- If the player should type a number greater than 4, the game accurately throws this message:
![Invalid Coordinates](images/invalid-coordinates.png)
If the player types "no" instead, the game will thank the player and end with a little pun. This is also tested and works correctly.
![Thank You](images/thanks-for-playing.png)

### Other Game Testing
- [Responsinator](http://www.responsinator.com/?url=https%3A%2F%2Fsea-dominion-cb02afeb3150.herokuapp.com%2F)
- [Am I responsive](https://ui.dev/amiresponsive?url=https://sea-dominion-cb02afeb3150.herokuapp.com/)
*These two sites are used to check if a web based app is responsive on all devices, ranging from mobile phones to desktop computers. All virtual representations of these devices work properly with this app.

## Technologies Used
- Python3

### Libraries used
- [Random](https://docs.python.org/3/library/random.html?highlight=random#module-random)

### Platforms used
- [Heroku](https://www.heroku.com/)

## Data model
- This game uses a class named Gameboard. This class represents the overall logic flow of the game and represents the entire board.

### Programs Used
- Github
- Gitpod
- Heroku
- PEP8
- VS Code

## Features left to implement.
- The option for the player to choose the size of the gameboard, with more rows and columns would be suitable for an updated version of this game.
-An option to place ships with different sizes on the board, offering the challenge of sinking the ships by hitting them more than once. For example if a ship is placed on row/ col [0,0] and [0,1] it would require the player to hit both coordinates to sink that ship.
- The option to welcome the player with a menu consisting of text-based art, provided by [ASCII Art](https://www.asciiart.eu/art-and-design/borders#google_vignette), looking something like this:
![welcomeascii](images/welcome.png)


## Known Bugs
- No current bugs known.

## Fixed Bugs
- Game declares Game Over after only 3 attempts, and throws message "You lost! All Your ships have been sunk".
- Game updates computer's score after player's attempts, leading to the Game Over situation.

## Deployment
* This project was deployed using Heroku.
- This is how to create the Heroku app:
- Log in to Heroku or create a new account.
- When on the main page, click the button called New in the top right corner and from the drop-down menu select "Create New App".
- Type in the name of the app, which must be unique to work.
- Select your region.
- Click the Create App button.
- Click the Settings Tab - scroll down to Config Vars.
- Click Reveal Config Vars and enter PORT into the Key box and 8000 into the Value box and click the Add button.

## Credits
- [Battleship game Python](https://github.com/SaraabbasiNZ/battleship-game-python/blob/main/run.py) This project was a great help for me to understand how the code logic works and how to operate the functions inside it.
- [Python Intermediate Project Assignment](https://www.youtube.com/watch?v=MgJBgnsDcF0&t=1145s) This video tutorial n how to build a battleships game very interesting and provided a lot of info on the subject. Even though it is 'intermediate', and maybe too advanced for me at the moment, it certainly gave inspiration for future projects.
- [word-Py](https://github.com/AliOKeeffe/word-Py) A great basic project for python based games which was very helpful for my project as well.

### Resources Used

#### Online Resources
- Youtube (Used to find tutorials and inpiration on the subject)
- W3CSchools (Used to find tips and information about python code)
- Stack Overflow (Used to find tips and information about python code)
- Pep8 (Used to check the code for syntax errors, indentation errors and warnings)
- TinyPNG (Used to compress images for this README file)
- Lucidchart (Used to create the flowchart image)
- Diffchecker (Used to compare old code with updated code)

#### Desktop resources
- VS Code (Used to write code locally and make a local safe copy of the code on the computer)

## Acknowledgments
- All the kind people in the Slack community which have provided alot of help and encouragement during the development of this project.
- My mentor Antonio for all the help, useful tips and recommendations.
