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
    files_list.append(file_name)


for file_name in files_list:
    df = pd.read_csv(file_name)
    puissance_tot = filter(df['puissance tot'])
    print(puissance_tot)

premier_fichier = input('premier fichier : ') + ".csv"
second_fichier = input("second fichier : ") + ".csv"
df1 = pd.read_csv(premier_fichier)
df2 = pd.read_csv(second_fichier)
puissance_tot1 = filter(df1['puissance tot'])
puissance_moy1 = df1['puissance tot moy'].iloc[-1]
ram_used1 = filter(df1['ram used'])
gpu_temp1 = filter(df1['gpu temp'])
cpu_temp1 = filter(df1['cpu temp'])
board_temp1 = filter(df1['board temp'])
perf1 = df1['perf'][0]
frug_list1 = []

puissance_tot2 = filter(df2['puissance tot'])
puissance_moy2 = df2['puissance tot moy'].iloc[-1]
ram_used2 = filter(df2['ram used'])
gpu_temp2 = filter(df2['gpu temp'])
cpu_temp2 = filter(df2['cpu temp'])
board_temp2 = filter(df2['board temp'])
perf2 = df2['perf'][0]
frug_list2 = []


for i in range(0,10):
    frug_list1.append(frug(i, perf1, puissance_moy1))
    frug_list2.append(frug(i, perf2, puissance_moy2))
   
#print values
print(puissance_moy1)
print(puissance_moy2)
print(perf1)
print(perf2)
print(frug_list1)
print(frug_list2)

fig, (ax1, ax2, ax3, ax4, ax6) = plt.subplots(5,1)

ax1.plot(puissance_tot1)
ax1.plot(puissance_tot2)
ax1.set_title("puissance tot (mW)")

ax2.plot(ram_used1)
ax2.set_title("ram used (%)")

ax3.plot(gpu_temp1)
ax3.set_title("gpu_temp (°C)")

ax4.plot(cpu_temp1)
ax4.set_title("cpu temp (°C)")

#ax5.plot(board_temp)
#ax5.set_title("board temp (°C)")

ax6.plot(frug_list1)
ax6.plot(frug_list2)
ax6.set_title("score de frugalité")

plt.show()
