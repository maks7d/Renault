import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def filter(s):
    mean = s.mean()
    std = s.std()
    return s[(s > mean - std) & (s < mean + 1.5*std)]

premier_fichier = input('premier fichier : ') + ".csv"
second_fichier = input("second fichier : ") + ".csv"
df1 = pd.read_csv(premier_fichier)
df2 = pd.read_csv(second_fichier)


puissance_tot = filter(df1['puissance tot'])
puissance_moy = df1['puissance tot moy'].iloc[-1]
ram_used = filter(df1['ram used'])
gpu_temp = filter(df1['gpu temp'])
cpu_temp = filter(df1['cpu temp'])
board_temp = filter(df1['board temp'])
perf = df1['perf'][0]

def frug(w):
    return perf - (w/(1+1/puissance_moy))

frug_list = []

for i in range(1,100):
    frug_list.append(frug(i))
    
print(frug_list)

fig, (ax1, ax2, ax3, ax4, ax6) = plt.subplots(5,1)

ax1.plot(puissance_tot)
ax1.set_title("puissance tot (mW)")

ax2.plot(ram_used)
ax2.set_title("ram used (%)")

ax3.plot(gpu_temp)
ax3.set_title("gpu_temp (°C)")

ax4.plot(cpu_temp)
ax4.set_title("cpu temp (°C)")

#ax5.plot(board_temp)
#ax5.set_title("board temp (°C)")

ax6.plot(frug_list)
ax6.set_title("score de frugalité")

plt.show()
