import matplotlib.pyplot as plt
import numpy


def draw_plot(source_file_name, label, color, iterations, interval=10, devinterval=100):
    source_file_name = source_file_name                                   # data file name
    label = label
    color = color
    interval = interval                                                   # every $interval iterations fitness is checked
    devinterval = devinterval                                             # interval for standard deviation
    iterations = iterations

    answers = {}
    for i in range(0, (iterations / interval) + 1):                 # create empty list of all fitness for given iteration
        answers[str(i * interval)] = []

    with open(source_file_name, "r") as data:                       # fill list created above
        for line in data:
            answers[line.split(";")[0]].append(float(line.split(";")[1]))

    x = range(0, iterations + 1)[0::interval]                       # create scale for means axis
    xdev = range(0, iterations + 1)[0::devinterval]                 # create scale for deviation axis
    means = []
    devmeans = []
    stddev = []

    for i in range(0, (iterations / interval) + 1):                 # count means
        means.append(numpy.mean(answers[str(i * interval)]))
    for i in range(0, (iterations / devinterval) + 1):              # count standard deviation
        stddev.append(numpy.std(answers[str(i * devinterval)]))
        devmeans.append(numpy.mean(answers[str(i * devinterval)]))

    plt.axhline(y=0)
    plt.plot(x, means, color=color, label=label)                    # draw plot
    plt.errorbar(xdev, devmeans, yerr=stddev, color=color, fmt='.') # draw standard deviation

    plt.axis([0, iterations, 0, 1700])
    plt.xlabel('Ilosc_iteracji')
    plt.ylabel('Dopasowanie')
    plt.legend()


def save_plot(plot_file_name):
    plot_file_name = plot_file_name
    # plt.show()
    plt.savefig(plot_file_name)

draw_plot("fitness_pyage.conf.femas_single_pyage.txt", "Femas single", "green", 1000)
draw_plot("fitness_pyage.conf.pso_basic_pyage.txt", "PSO basic", "blue", 1000)
draw_plot("fitness_pyage.conf.femas_pso_pyage.txt", "Femas PSO", "red", 1000)
save_plot("compared.png")