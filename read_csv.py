import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

def filter(s):
    mean = s.mean()
    std = s.std()
    return s[(s > mean - std) & (s < mean + 1.5*std)]

def frug(w, perf, puissance_moy):
    return  (perf - round(perf,1)) - w/puissance_moy

files_list = []

while True:
    file_name = input("nom du fichier('Entrée pour terminer') : ")
    if not file_name:
        break
    files_list.append(file_name + ".csv")

frug_list = []

fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5,1)

for file_name in files_list:
    df = pd.read_csv(file_name)
    puissance_tot = filter(df['puissance tot'])
    puissance_moy = df['puissance tot moy'].iloc[-1]
    ram_used = filter(df['ram used'])
    gpu_temp = filter(df['gpu temp'])
    cpu_temp = filter(df['cpu temp'])
    board_temp = filter(df['board temp'])
    perf = df['perf'][0]

    for i in range(0,10):
        frug_list.append(frug(i, perf, puissance_moy))

    ax1.plot(puissance_tot)
    ax2.plot(puissance_moy)
    ax3.plo(ram_used)
    ax4.plot(gpu_temp)
    ax5.plot(cpu_temp)

plt.show()
