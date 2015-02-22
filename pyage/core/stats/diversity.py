from math import sqrt


def compute_diversity(self, agents):
    agents_max = []
    sum_jong = 0.0
    jong_values = []

    for a in agents:
        agent_genotypes = [ag.get_genotype().genes for ag in a.get_agents()]
        avg_vals = [0] * len(agent_genotypes[0])
        pow_sum_vals = [0] * len(agent_genotypes[0])
        for gen in agent_genotypes:
            for i, g in enumerate(gen):
                avg_vals[i] += g
                pow_sum_vals[i] += g * g

        values = []
        for i in range(len(avg_vals)):
            avg_vals[i] /= len(agent_genotypes)
            values.append(sqrt(round(pow_sum_vals[i]/len(agent_genotypes)-avg_vals[i]*avg_vals[i], 7)))

        jong_value = 0.0
        for gen in agent_genotypes:
            for i, g in enumerate(gen):
                val = (g - avg_vals[i])**2
                jong_value += val
                sum_jong += val
        jong_values.append(jong_value)
        agents_max.append(max(values))

    return max(agents_max), sum_jong