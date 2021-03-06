# coding=utf-8
import logging
import os

from pyage.core import address
from pyage.core.agent.agent import unnamed_agents
from pyage.core.agent.aggregate import AggregateAgent
from pyage.core.emas import EmasService
from pyage.core.emaspso import EmasPsoService
from pyage.core.locator import TorusLocator
from pyage.core.migration import ParentMigration
from pyage.core.stats.gnuplot import StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition
from pyage.solutions.evolution.crossover import SinglePointCrossover
from pyage.solutions.evolution.evaluation import FloatRastriginEvaluation
from pyage.solutions.evolution.initializer import float_emas_initializer
from pyage.solutions.evolution.mutation import NormalMutation, UniformFloatMutation


logger = logging.getLogger(__name__)

agents_count = int(os.environ['AGENTS'])
logger.debug("EMAS, %s agents", agents_count)
agents = unnamed_agents(agents_count, AggregateAgent)

stop_condition = lambda: StepLimitStopCondition(3001)

aggregated_agents = lambda: float_emas_initializer(40, energy=100, size=int(360/agents_count), lowerbound=-10, upperbound=10)

emas = EmasPsoService

minimal_energy = lambda: 0
reproduction_minimum = lambda: 90
migration_minimum = lambda: 120
newborn_energy = lambda: 100
transferred_energy = lambda: 40

global_velocity = lambda: 0.4
local_velocity = lambda: 0.2
random_velocity = lambda: 0.01
old_velocity = lambda: 0.4

evaluation = FloatRastriginEvaluation
crossover = SinglePointCrossover
mutation = lambda: UniformFloatMutation(probability=1, radius=1)

address_provider = address.SequenceAddressProvider

migration = ParentMigration

locator = lambda: TorusLocator(10, 10)

stats = lambda: StepStatistics('fitness_%s_pyage.txt' % __name__, 'count_%s_pyage.txt' % __name__, 'diversity_%s_pyage.txt' % __name__)
