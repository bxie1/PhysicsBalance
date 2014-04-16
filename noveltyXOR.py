#Authors: Ben Xie and Tyler Zon

import math
import cPickle as pickle
from noveltySearch import *
from neat import config, population, chromosome, genome, visualize
from neat.nn import nn_pure as nn

config.load('xor_config')

chromosome.node_gene_type = genome.NodeGene

INPUTS = [[0, 0], [0, 1], [1, 0], [1, 1]]
OUTPUTS = [0, 1, 1, 0]



n = NoveltySearch(10, 150, 0.3)

def eval_fitness(population):
    """
    Create a fitness function that returns higher values for better
    solutions.  For this task, we first calculate the sum-squared
    error of a network on the XOR task.  Good networks will have
    low error, so the fitness is 1 - sqrt(avgError).
    """

    for chromo in population:
        brain = nn.create_ffphenotype(chromo)
        error = 0.0
        
        #create 4d vector
        p = []
        
        # for each of the 4 inputs...
        for i, inputs in enumerate(INPUTS):
            brain.flush()
            output = brain.sactivate(inputs)
            error += (output[0] - OUTPUTS[i])**2
            
            # put the outputs in the point
            p.append(output[0])
        
        #set fitness to the sparseness
        chromo.fitness = n.addToArchive(p)

        #sparseness = n.sparseness(p)
        progress = 1 - math.sqrt(error/len(OUTPUTS))
        # set progress to sparseness
        
        if progress > 0.9:
            print "Solution found!"
            print "Progress: " + str(progress)
            chromo.fitness = 1.5 # trigger max_fitness threshold
            f = open("novelty_chromo", "w")
            pickle.dump(chromo, f)
            f.close()
        

# Tell NEAT that we want to use the above function to evaluate fitness
population.Population.evaluate = eval_fitness

# Create a population (the size is defined in the configuration file)
pop = population.Population()

# It will stop if fitness surpasses the max_fitness_threshold in config file
pop.epoch(70, report=True, save_best=False)

n.saveArchive("archive.dat")

# Plots the evolution of the best/average fitness
visualize.plot_stats(pop.stats)

# Visualizes speciation
visualize.plot_species(pop.species_log)
