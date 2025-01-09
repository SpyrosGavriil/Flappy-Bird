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

## NEAT Configuration Overview
The NEAT algorithm's behavior is controlled using the `config/config-feedforward.txt` file. Key sections include:

- **[NEAT]**: Defines core settings like `pop_size` (population size) and `fitness_threshold`.
- **[DefaultGenome]**: Specifies how the genome evolves, including mutation rates and node activation functions.
- **[DefaultStagnation]**: Controls when species are considered stagnant and removed from the population.
- **[DefaultReproduction]**: Manages how genomes are selected and bred for the next generation.

For a detailed explanation of the configuration file, refer to the [NEAT-Python documentation](https://neat-python.readthedocs.io/en/latest/config_file.html).

## License
This project is licensed under the MIT License.
