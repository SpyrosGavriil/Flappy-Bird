import pygame
import neat
import os
from bird import Bird
from pipe import Pipe
from base import Base
from utils import draw_window

# Base directory setup (one level above 'src/')
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Navigate to the root project folder
CONFIG_PATH = os.path.join(BASE_DIR, "config", "config-feedforward.txt")

WIN_WIDTH = 500
WIN_HEIGHT = 800
GEN = 0 # Global generation counter for tracking generations in NEAT

def fitness(genomes, config):
    global GEN
    GEN += 1  # Increment generation count
    nets = []  # Store neural networks
    ge = []  # Store genome objects for fitness modification
    birds = []  # List of bird objects
    
    # Initialize genomes and networks
    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(230, 350))
        g.fitness = 0
        ge.append(g)
        
    
    base = Base(730)
    pipes = [Pipe(600)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    run = True
    clock = pygame.time.Clock()

    score = 0

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        
        # Determine which pipe to check for collision
        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width(): # If the bird passed the pipe check the 2nd pipe if it exists
                pipe_ind = 1
        else:
            run = False # If no birds are left, end the game
            break        
                
        # Move birds and evaluate decisions using the neural network    
        for x, bird in enumerate(birds):
            bird.move()
            ge[x].fitness += 0.1 # Reward surviving birds slightly
            
            output = nets[x].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom)))
            
            if output[0] > 0.5: # If the neural network output is > 0.5, bird jumps
                bird.jump()
        
        # Pipe collision and movement logic
        add_pipe = False
        rem = [] # List to remove pipes
        for pipe in pipes:
            for x, bird in enumerate(birds):
                if pipe.collide(bird): # Check if bird collides with the pipe
                    ge[x].fitness -= 1 # Penalize the bird for collision
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            # Remove pipes that have gone out of screen
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            pipe.move()

        if add_pipe:
            score += 1
            for g in ge:
                g.fitness += 5 # Reward passing a pipe
            pipes.append(Pipe(600))

        for r in rem:
            pipes.remove(r)

        for x, bird in enumerate(birds):
            if bird.y + bird.img.get_height() >= 730 or bird.y < 0:
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)
                
        if score > 50:
            break

        base.move()
        draw_window(win, birds, pipes, base, score, GEN)

def run(config_path):
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path,
    )

    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    p.run(fitness, 50)

if __name__ == "__main__":
    pygame.init()
    run(CONFIG_PATH)