import logging
import random

from pyage.core.address import Addressable
from pyage.core.agent.aggregate import get_random_move
from pyage.core.inject import Inject, InjectWithDefault


logger = logging.getLogger(__name__)


class PsoAgent(Addressable):
    # @Inject("migration", "evaluation", "crossover", "mutation", "pso", "transferred_energy")
    @Inject("evaluation", "pso", "global_velocity", "local_velocity", "random_velocity")
    def __init__(self, genotype, energy, name=None):
        self.name = name
        super(PsoAgent, self).__init__()
        self.genotype = genotype
        self.energy = energy
        self.steps = 0
        self.dead = False
        self.evaluation.process([genotype])
        self.psoParams = {"global_fitness": -99999999.9, "local_fitness": -99999999.9}

    def step(self):
        self.steps += 1
        if self.steps > 1:
            self.update_global()
            self.update_local()
            self.move_particle()

    def move_particle(self):
        new_genes = []
        for i in range(len(self.genotype.genes)):
            old_gene = self.genotype.genes[i]
            velocity = self.global_velocity * (self.psoParams["global_genotype"][i] - old_gene) + self.local_velocity * (self.psoParams["local_genotype"][i] - old_gene) + self.random_velocity * (random.uniform(-5, 5) - old_gene)
            # velocity = (0.5 * (self.psoParams["global_genotype"][i] - old_gene)) + (0.5 * (self.psoParams["local_genotype"][i] - old_gene))
            new_genes.append(old_gene + velocity)
            logger.debug("old gene: "+str(old_gene)+", velocity: "+str(velocity)+", new gene: "+str(new_genes[i]))
        self.genotype.genes = new_genes
        self.evaluation.process([self.genotype])

    def get_fitness(self):
        return self.genotype.fitness

    def get_best_genotype(self):
        return self.genotype

    def get_genotype(self):
        return self.genotype

    def update_local(self):
        if self.get_fitness() > self.psoParams["local_fitness"]:
            self.psoParams["local_fitness"] = self.get_fitness()
            self.psoParams["local_genotype"] = self.get_genotype().genes

    def update_global(self):
        for agent in self.parent.get_agents():
            if agent.get_fitness() > self.psoParams["global_fitness"]:
                self.psoParams["global_fitness"] = agent.get_fitness()
                self.psoParams["global_genotype"] = agent.get_genotype().genes

    def __repr__(self):
        return "<PsoAgent@%s>" % self.get_address()


class PsoService(object):
    # @Inject("minimal_energy", "reproduction_minimum", "migration_minimum", "newborn_energy")
    # @InjectWithDefault(("move_probability", 0.1))
    def __init__(self):
        super(PsoService, self).__init__()
    #
    # def should_move(self, agent):
    #     return random.random() < self.move_probability
