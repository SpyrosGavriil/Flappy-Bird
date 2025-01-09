# Flappy Bird with NEAT AI

A Python project using Pygame and NEAT to create an AI that learns to play Flappy Bird.

## Project Structure
- `src/`: Contains the Python source code.
- `imgs/`: Contains game assets (bird, pipes, background).
- `config/`: Contains the NEAT configuration file.
- `requirements.txt`: List of required Python packages.
- `.gitignore`: Specifies files to be ignored by Git.

## How to Run the Project

1. Clone the repository:
   ```
   git clone <your-repo-url>
   cd Flappy-Bird
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the game:
   ```
   python src/main.py
   ```

## How the AI Works
The AI uses the NEAT (NeuroEvolution of Augmenting Topologies) algorithm to train a neural network for playing Flappy Bird. Each bird (agent) is controlled by a neural network that learns over multiple generations.

## License
This project is licensed under the MIT License.
