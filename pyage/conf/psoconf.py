# coding=utf-8
import logging
import os

from pyage.core import address
from pyage.core.agent.agent import unnamed_agents
from pyage.core.agent.aggregate import AggregateAgent
from pyage.core.pso import PsoService
from pyage.core.locator import TorusLocator
from pyage.core.stats.gnuplot import StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition
from pyage.solutions.evolution.evaluation import FloatRastriginEvaluation
from pyage.solutions.evolution.initializer import pso_initializer


logger = logging.getLogger(__name__)

agents_count = 1 #int(os.environ['AGENTS'])
logger.debug("PSO, %s agents", agents_count)
agents = unnamed_agents(agents_count, AggregateAgent)

stop_condition = lambda: StepLimitStopCondition(1001)

aggregated_agents = lambda: pso_initializer(40, energy=100, size=10, lowerbound=-10, upperbound=10)

pso = PsoService

global_velocity = lambda: 0.5
local_velocity = lambda: 0.5
random_velocity = lambda: 0.1


evaluation = FloatRastriginEvaluation
# crossover = SinglePointCrossover
# mutation = NormalMutation

address_provider = address.SequenceAddressProvider

# migration = ParentMigration

locator = lambda: TorusLocator(10, 10)

stats = lambda: StepStatistics('fitness_%s_pyage.txt' % __name__)
