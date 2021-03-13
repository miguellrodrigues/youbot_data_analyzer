import json
import matplotlib.pyplot as plt
from os import listdir, mkdir
from os.path import exists

fig = plt.figure()

ax1 = fig.add_subplot()


path = "./data_in/"
save_path = "./data_out/"

if not exists(save_path):
    mkdir(save_path)

for data_file in listdir(path):
    with open(path + data_file) as file:
        data = json.load(file)

    fitness_list = data["generations_fitness"]

    ax1.plot(range(len(fitness_list)), fitness_list)

    plt.savefig("./data_out/{}.png".format(data_file.replace(".json", '')), dpi=600, format='png', bbox_inches='tight')

    ax1.clear()

    file.close()

