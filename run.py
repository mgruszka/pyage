import os
import subprocess
from timeit import timeit
import shutil
from draw_plot import draw_plot, save_plot

def compare_all(plot_type, iterations, ylabel, agents):
    draw_plot(plot_type + "_pyage.conf.femas_single_pyage.txt", "Femas single", "green", iterations, ylabel)
    draw_plot(plot_type + "_pyage.conf.pso_basic_pyage.txt", "PSO basic", "blue", iterations, ylabel)
    draw_plot(plot_type + "_pyage.conf.femas_pso_pyage.txt", "Femas PSO", "red", iterations, ylabel)
    draw_plot(plot_type + "_pyage.conf.pso_neighborhood_pyage.txt", "PSO neighborhood", "yellow", iterations, ylabel)
    save_plot("plots/compared_" + plot_type + str(agents) + ".png")

def draw_plots(file_name, plot_name, color, iterations):
    draw_plot("fitness_pyage.conf." + file_name, plot_name, color, iterations, "Dopasowanie")
    save_plot("plots/" + file_name + "_fitness.png")
    draw_plot("count_pyage.conf." + file_name, plot_name, color, iterations, "Liczebnosc_populacji")
    save_plot("plots/" + file_name + "_count.png")
    draw_plot("msd_diversity_pyage.conf." + file_name, plot_name, color, iterations, "Roznorodnosc MSD")
    save_plot("plots/" + file_name + "_msd_diversity.png")
    draw_plot("moi_diversity_pyage.conf." + file_name, plot_name, color, iterations, "Roznorodnosc MOI")
    save_plot("plots/" + file_name + "_moi_diversity.png")


def move_files_to_folder(agents):
    destination = "/home/gruszek/magisterka/pyage/plots/3000iterAgents"+str(agents)
    os.makedirs(destination)
    source = os.listdir("/home/gruszek/magisterka/pyage/")
    for files in source:
        if files.endswith(".txt"):
            shutil.move(files, destination)
    # subprocess.call("sleep 5", shell=True)
    # source = os.listdir("/home/gruszek/magisterka/pyage/plots/")
    # for files in source:
    #     if files.endswith(".png"):
    #         shutil.move(files, destination)


# for agents in [1, 3, 6, 9, 12]:
#     os.environ['AGENTS'] = str(agents)
#     print("######Number of AGENTS: " + str(agents))
#     for i in range(1, 11):
#         subprocess.check_call(['time', 'python', '-m', 'pyage.core.bootstrap', 'pyage.conf.femas_single'])
#         subprocess.check_call(['time', 'python', '-m', 'pyage.core.bootstrap', 'pyage.conf.femas_pso'])
#         subprocess.check_call(['time', 'python', '-m', 'pyage.core.bootstrap', 'pyage.conf.pso_basic'])
#         subprocess.check_call(['time', 'python', '-m', 'pyage.core.bootstrap', 'pyage.conf.pso_neighborhood'])
#     compare_all("fitness", 3000, "Fitness", agents)
#     compare_all("count", 3000, "Liczebnosc_populacji", agents)
#     compare_all("msd_diversity", 3000, "Roznorodnosc MSD", agents)
compare_all("moi_diversity", 3000, "Roznorodnosc MOI", '9fixed')
    # move_files_to_folder(agents)

# draw_plots("femas_single_pyage.txt", "Femas single", "green", 1000)
# draw_plots("pso_basic_pyage.txt", "PSO basic", "blue", 1000)
# draw_plots("femas_pso_pyage.txt", "Femas PSO", "red", 1000)
# draw_plots("pso_neighborhood_pyage.txt", "PSO neighborhood", "yellow", 1000)

