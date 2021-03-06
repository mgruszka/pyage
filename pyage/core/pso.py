import logging
import random

from pyage.core.address import Addressable
from pyage.core.inject import Inject


logger = logging.getLogger(__name__)


class PsoAgent(Addressable):
    @Inject("evaluation", "pso", "global_velocity", "local_velocity", "old_velocity", "random_velocity", "stop_condition")
    def __init__(self, genotype, name=None):
        self.name = name
        super(PsoAgent, self).__init__()
        self.genotype = genotype
        self.two_old_gene = genotype
        self.steps = 0
        self.evaluation.process([genotype])
        self.psoParams = {"global_fitness": -99999999.9, "local_fitness": -99999999.9}
        self.inertia = 1

    def step(self):
        self.steps += 1
        self.inertia = 1 - (self.steps / self.stop_condition.step_limit)
        # self.interia = 1
        if self.steps > 1:
            self.update_global()
            self.update_local()
            self.move_particle()

    def move_particle(self):
        new_genes = []
        global_v = self.global_velocity * self.inertia
        local_v = self.local_velocity * self.inertia
        old_v = self.old_velocity * self.inertia
        random_v = self.random_velocity * self.inertia
        for i in range(len(self.genotype.genes)):
            old_gene = self.genotype.genes[i]
            two_old_gene = self.two_old_gene.genes[i]
            velocity = global_v * (self.psoParams["global_genotype"][i] - old_gene) + local_v * (self.psoParams["local_genotype"][i] - old_gene) + old_v * (two_old_gene - old_gene) + random_v * (random.uniform(-5, 5) - old_gene)
            new_genes.append(old_gene + velocity)
            self.two_old_gene.genes[i] = old_gene
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
    def __init__(self):
        super(PsoService, self).__init__()
