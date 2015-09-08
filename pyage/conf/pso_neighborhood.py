# coding=utf-8
import logging

from pyage.core import address
from pyage.core.agent.agent import unnamed_agents
from pyage.core.agent.aggregate import AggregateAgent
from pyage.core.pso import PsoService
from pyage.core.locator import TorusLocator
from pyage.core.psoneighborhood import PsoNeighborhoodService
from pyage.core.stats.gnuplot import StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition
from pyage.solutions.evolution.evaluation import FloatRastriginEvaluation
from pyage.solutions.evolution.initializer import pso_initializer


logger = logging.getLogger(__name__)

agents_count = 1
logger.debug("PSO, %s agents", agents_count)
agents = unnamed_agents(agents_count, AggregateAgent)

stop_condition = lambda: StepLimitStopCondition(3001)

aggregated_agents = lambda: pso_initializer(40, size=int(360/agents_count), lowerbound=-10, upperbound=10)

pso = PsoNeighborhoodService

global_velocity = lambda: 0.4
neighbor_velocity = lambda: 0.4
local_velocity = lambda: 0.2
random_velocity = lambda: 0.01
old_velocity = lambda: 0.4


evaluation = FloatRastriginEvaluation

address_provider = address.SequenceAddressProvider

locator = lambda: TorusLocator(10, 10)

stats = lambda: StepStatistics('fitness_%s_pyage.txt' % __name__, 'count_%s_pyage.txt' % __name__, 'diversity_%s_pyage.txt' % __name__)

