import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

#filtrage d'une liste en ne gardant que les valeurs comprises entre la moyenne et - et +*1.5l'ecart type
def filter(s):
    mean = s.mean()
    std = s.std()
    return s[(s > mean - std) & (s < mean + 1.5*std)]

#calcul du score de frugalité
def frug(w, perf, puissance_moy):
    return perf - w/(1+1/puissance_moy) 


files_list = []

#entrer nom de fichier tant que l'utilisateur rentre une chaine de caracteres
while True:
    file_name = input("nom du fichier('Entrée pour terminer') : ")
    if not file_name:
        break
    files_list.append(file_name + ".csv")

frug_list = []

fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5,1)

#traitement du fichier et affichage des plot
for file_name in files_list:
    df = pd.read_csv(file_name)
    puissance_tot = filter(df['puissance tot'])
    puissance_moy = df['puissance tot moy'].iloc[-1]
    ram_used = filter(df['ram used'])
    gpu_temp = filter(df['gpu temp'])
    cpu_temp = filter(df['cpu temp'])
    board_temp = filter(df['board temp'])
    perf = df['perf'][0]

    frug_list.clear()
    for i in range(0,1,10):
        frug_list.append(frug(i, perf, puissance_moy))

    ax1.plot(puissance_tot)
    ax2.plot(ram_used)
    ax3.plot(gpu_temp)
    ax4.plot(cpu_temp)
    ax5.plot(frug_list)
    print(frug_list)
plt.show()
