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

def genetic_algorithm(target_string, population_size, mutation_rate, max_generations, elitism=False):
  # This is the main function, it runs the whole thing
  population = [generate_random_string(len(target_string)) for _ in range(population_size)]
  generation = 0
  fitness_history = []

  # This loop keeps going until we find the target string or run out of tries
  while generation < max_generations:
    # Sort the population by how close they are to the target string
    population = sorted(population, key=lambda x: fitness(target_string, x), reverse=True)
    fittest_individual = population[0]
    fitness_history.append(fitness(target_string, fittest_individual))

    # We found it! Exit loop
    if fittest_individual == target_string:
      break

    # Here's where it gets interesting, creating the next generation
    new_population = [fittest_individual] if elitism else []  # Keep the best one if elitism is on

    # Loop to create new population by breeding the current ones
    for _ in range(population_size - 1):
      parent1 = random.choice(population[:int(population_size / 2)])
      parent2 = random.choice(population[:int(population_size / 2)])
      child = crossover(parent1, parent2)
      child = mutate(child, mutation_rate)
      new_population.append(child)

    # The new generation becomes the old population
    population = new_population
    generation += 1

    # Print update on progress (commented out, might slow things down)
    # print(f"Generation {generation}: Best Individual - {fittest_individual}")

  # Return the best string we found and how close it was over generations
  return fittest_individual, fitness_history

def plot_fitness_history(fitness_history, title):
  # This function makes a graph showing how close we got over time
  plt.plot(range(len(fitness_history)), fitness_history)
  plt.title(title)
  plt.xlabel("Generation")
  plt.ylabel("Fitness")
  plt.show()