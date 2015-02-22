import subprocess
from draw_plot import draw_plot, save_plot

def compare_all(plot_type, iterations, ylabel):
    draw_plot(plot_type + "_pyage.conf.femas_single_pyage.txt", "Femas single", "green", iterations, ylabel)
    draw_plot(plot_type + "_pyage.conf.pso_basic_pyage.txt", "PSO basic", "blue", iterations, ylabel)
    draw_plot(plot_type + "_pyage.conf.femas_pso_pyage.txt", "Femas PSO", "red", iterations, ylabel)
    save_plot("plots/compared_" + plot_type + ".png")

def draw_plots(file_name, plot_name, color, iterations):
    draw_plot("fitness_pyage.conf." + file_name, plot_name, color, iterations, "Dopasowanie")
    save_plot("plots/" + file_name + "_fitness.png")
    draw_plot("count_pyage.conf." + file_name, plot_name, color, iterations, "Liczebnosc_populacji")
    save_plot("plots/" + file_name + "_count.png")
    draw_plot("msd_diversity_pyage.conf." + file_name, plot_name, color, iterations, "Roznorodnosc MSD")
    save_plot("plots/" + file_name + "_msd_diversity.png")
    draw_plot("moi_diversity_pyage.conf." + file_name, plot_name, color, iterations, "Roznorodnosc MOI")
    save_plot("plots/" + file_name + "_moi_diversity.png")

for i in range(1, 5):
    subprocess.check_call(['python', '-m', 'pyage.core.bootstrap', 'pyage.conf.femas_single'])
    subprocess.check_call(['python', '-m', 'pyage.core.bootstrap', 'pyage.conf.femas_pso'])
    subprocess.check_call(['python', '-m', 'pyage.core.bootstrap', 'pyage.conf.pso_basic'])

draw_plots("femas_single_pyage.txt", "Femas single", "green", 1000)
draw_plots("pso_basic_pyage.txt", "PSO basic", "blue", 1000)
draw_plots("femas_pso_pyage.txt", "Femas PSO", "red", 1000)

compare_all("fitness", 1000, "Dopasowanie")
compare_all("count", 1000, "Liczebnosc_populacji")
compare_all("msd_diversity", 1000, "Roznorodnosc MSD")
compare_all("moi_diversity", 1000, "Roznorodnosc MOI")