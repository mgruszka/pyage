import matplotlib.pyplot as plt
import numpy


def draw_plot(source_file_name, label, color, iterations, ylabel, interval=10, devinterval=100):
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


    yheight = 1.3 * max(means)
    plt.axis([0, iterations, 0, yheight])
    if "moi" in source_file_name:
        plt.yscale('log')
    plt.xlabel('Ilosc_iteracji')
    plt.ylabel(ylabel)
    if "count" in source_file_name:
        plt.legend(loc=3)
    else:
        plt.legend()


def save_plot(plot_file_name):
    plot_file_name = plot_file_name
    # plt.show()
    plt.savefig(plot_file_name)
    plt.close()
