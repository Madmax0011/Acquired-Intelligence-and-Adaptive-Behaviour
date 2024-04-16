import random
import string
import matplotlib.pyplot as plt

# This is the string we're trying to evolve, basically our target
TARGET_STRING = "Hello, World! My name is Shriyansh Nautiyal "
POPULATION_SIZE = 100
MAX_GENERATIONS = 1000
MUTATION_RATE = 0.2

def generate_random_string(length):
  return ''.join(random.choice(string.printable) for _ in range(length))

def fitness(target, test):
  # This function checks how close a random string is to our target
  # Basically counting how many letters match
  score = sum(1 for t, i in zip(target, test) if t == i)
  return score / len(target)

def crossover(parent1, parent2):
  # This function mixes two random strings from our population
  # Like splicing DNA in biology class, but with letters
  crossover_point = random.randint(0, len(parent1) - 1)
  child = parent1[:crossover_point] + parent2[crossover_point:]
  return child

def mutate(child, mutation_rate):
  # This function randomly changes some letters in the child string
  # Like mistakes during copying DNA, but hopefully for the better here
  mutated_child = "".join(
      random.choice(string.printable) if random.random() < mutation_rate else char for char in child
  )
  return mutated_child

