# GameInt: Code-Breaking Game

GameInt is a two-player code-breaking game where one player acts as the codemaker by concealing four colored pins, and the other player acts as the codebreaker by attempting to guess the concealed pegs.

The code maker, in this case, the system, sets four colored pegs represented by integers from 1 to 6 (1-White, 2-Blue, 3-Red, 4-Yellow, 5-Green, and 6-Purple) behind a viewing screen. The system generates a four-digit number at random to represent the concealed pegs.

The codebreaker, on the other hand, tries to discover the hidden pegs by entering four digits. To win the game, the codebreaker must correctly identify both the color and position of the pegs.

## How to Play

1. **Code Maker (System):**
   - The system randomly generates a four-digit number representing the concealed pegs.
   - Each digit in the number corresponds to a specific color: 1-White, 2-Blue, 3-Red, 4-Yellow, 5-Green, 6-Purple.

2. **Code Breaker (Player):**
   - The player enters a four-digit number to guess the concealed pegs.
   - After each guess, the system provides feedback using 'black' pegs ('1') and 'white' pegs ('0') to indicate the correctness of the guessed colors and positions.
   - If the guessed pegs are the correct color and in the right location, the system uses the 'black' peg.
   - If the guessed pegs are the correct color but in the wrong location, the system uses the 'white' peg.
   - If the color is incorrect, the system does not use any pegs.

3. **Winning the Game:**
   - The game continues until the codebreaker correctly guesses all four pegs in the correct order.
   - The codebreaker wins the game if they can accurately identify the color and position of all pegs within a certain number of guesses.

## Technologies Used

- **Python:** Core programming language used for implementing the game logic.
- **Random Module:** Utilized to generate a random code for the system.
- **Console Input/Output:** Interaction with the player through the console.

## How to Run

1. Clone the repository.

2. Navigate to the project directory.

3. Run the Python script.


## Contribution Guidelines

Contributions to the project are welcome! If you find any bugs, have suggestions for improvements, or would like to add new features, please feel free to open an issue or submit a pull request.
