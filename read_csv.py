import pandas as pd
import matplotlib.pyplot as plt

#filtrage d'une liste en ne gardant que les valeurs comprises entre la moyenne et - 1 et +1.5 l'ecart type
def filter(s):
    mean = s.mean()
    std = s.std()
    return s[(s > mean - std) & (s < mean + 1.5*std)]

#calcul du score de frugalité
def frug(w, perf, puissance_moy):
    return w/(perf*puissance_moy)

files_list = []
frug_list = []

#entrer nom de fichier tant que l'utilisateur rentre une chaine de caracteres
while True:
    file_name = input("nom du fichier('Entrée pour terminer') : ")
    if not file_name:
        break
    files_list.append(file_name + ".csv")

fig, axs = plt.subplots(3,2)

#ouverture/traitement du fichier et affichage des plot
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
    for i in range(-10,10):
        frug_list.append(frug(i, perf, puissance_moy))

    axs[0,0].plot(puissance_tot)
    axs[0,0].set_title('puissance totale')
    axs[0,1].plot(ram_used)
    axs[0,1].set_title("ram used(%)")
    axs[1,0].plot(gpu_temp)
    axs[1,0].set_title("gpu temperature")
    axs[1,1].plot(cpu_temp)
    axs[1,1].set_title("cpu temperature")
    axs[2,1].plot(frug_list)
    axs[2,1].set_title("score de frugalité")

    fig.tight_layout()
    #print(frug_list)

plt.show()
