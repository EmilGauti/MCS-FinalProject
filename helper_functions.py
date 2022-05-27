import numpy as np
class Bob():
    def __init__(self):
        self.speed=1.0
        self.mass=1.0
        self.vision=0.01#Only a fraction of the grid
        self.previous_bob = None
    def mutate(self,mutation_rate):
        self.previous_bob = copy(self)#Need to figure it out
        self.speed = self.speed + np.random.uniform(-mutation_rate[0],mutation_rate[0])
        self.mass = self.mass + np.random.uniform(-mutation_rate[1],mutation_rate[1])
        self.vision = self.vision + np.random.uniform(-mutation_rate[2],mutation_rate[2])
