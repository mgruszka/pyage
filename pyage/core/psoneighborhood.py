import logging
import random

from pyage.core.address import Addressable
from pyage.core.inject import Inject


logger = logging.getLogger(__name__)


class PsoAgent(Addressable):
    @Inject("evaluation", "pso", "global_velocity", "neighbor_velocity", "local_velocity", "random_velocity", "stop_condition")
    def __init__(self, genotype, name=None):
        self.name = name
        super(PsoAgent, self).__init__()
        self.genotype = genotype
        self.steps = 0
        self.evaluation.process([genotype])
        self.psoParams = {"global_fitness": -99999999.9, "local_fitness": -99999999.9, "neighbor_fitness": -99999999.9}
        self.inertia = 1

    def step(self):
        self.steps += 1
        self.inertia = 1 - (self.steps / self.stop_condition.step_limit)
        if self.steps > 1:
            self.update_global()
            self.update_local()
            self.update_neighbor()
            self.move_particle()

    def move_particle(self):
        new_genes = []
        global_v = self.global_velocity * self.inertia
        neighbor_v = self.neighbor_velocity * self.inertia
        local_v = self.local_velocity * self.inertia
        random_v = self.random_velocity * self.inertia
        for i in range(len(self.genotype.genes)):
            old_gene = self.genotype.genes[i]
            velocity = global_v * (self.psoParams["global_genotype"][i] - old_gene) + neighbor_v * (self.psoParams["neighbor_genotype"][i] - old_gene) + local_v * (self.psoParams["local_genotype"][i] - old_gene) + random_v * (random.uniform(-5, 5) - old_gene)
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

    def update_neighbor(self):
        self.psoParams["neighbor_fitness"] = -99999999.9
        for agent in self.parent.get_neighbours():
            if agent.get_fitness() > self.psoParams["neighbor_fitness"]:
                self.psoParams["neighbor_fitness"] = agent.get_fitness()
                self.psoParams["neighbor_genotype"] = agent.get_genotype().genes

    def __repr__(self):
        return "<PsoAgent@%s>" % self.get_address()


class PsoNeighborhoodService(object):
    def __init__(self):
        super(PsoNeighborhoodService, self).__init__()
