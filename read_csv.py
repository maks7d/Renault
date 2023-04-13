import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

nom_fichier = input('nom du fichier : ') + ".csv"

df = pd.read_csv(nom_fichier)

puissance_tot = df['puissance tot']
ram_used = df['ram used']
gpu_temp = df['gpu temp']
cpu_temp = df['cpu temp']
board_temp = df['board temp']

fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5,1)

ax1.plot(puissance_tot)
ax1.set_title("puissance tot (mW)")

ax2.plot(ram_used)
ax2.set_title("ram used (%)")

ax3.plot(gpu_temp)
ax3.set_title("gpu_temp (°C)")

ax4.plot(cpu_temp)
ax4.set_title("cpu temp (°C)")

ax5.plot(board_temp)
ax5.set_title("board temp (°C)")

plt.show()
