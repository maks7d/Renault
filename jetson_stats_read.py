from jtop import jtop 
import csv
import os
#declaration des listes contenant les données mesurées
power_tot_list = []
power_tot_avg_list = []
ram_list = []
gpu_temp_list = []
cpu_temp_list = []
board_temp_list = []
perf_list = []

#déclaration des entetes du fichier csv dans lequel seront enregistrées les données
entetes = ['puissance tot', 'puissance tot moy', 'ram used', 'gpu temp', 'cpu temp', 'board temp', 'perf']

#nombre de valeurs ajoutés dans les listes
value_counts = 0


with jtop() as jetson:
    # jetson.ok() will provide the proper update frequency
    while jetson.ok():
        os.system('clear')
        print("running...")

        # lit et affiche les stats de la jetson
        print("puissance totale : ", int(jetson.power['tot']['power'])/1000, "W") 
        print("puissance totale moyenne: ", int(jetson.power['tot']['avg'])/1000, "W") 
        print("fréquence gpu : ", int(jetson.gpu['ga10b']['freq']['cur'])/1000, "MHz") 
        print("temperature gpu : ", jetson.temperature['GPU']['temp'], "°C") 
        print("temperature cpu : ", jetson.temperature['CPU']['temp'], "°C")
        print("temperature carte : ", jetson.temperature['Tboard']['temp'], "°C")
        print("ram used : ", round(jetson.memory['RAM']['used']/jetson.memory['RAM']['tot']*100,2), "%")
        
        #ajout des stats aux listes respectives
        power_tot_list.append(jetson.power['tot']['power'])
        power_tot_avg_list.append(jetson.power['tot']['avg'])
        ram_list.append(round(jetson.memory['RAM']['used']/jetson.memory['RAM']['tot']*100,1))
        gpu_temp_list.append(jetson.temperature['GPU']['temp'])
        cpu_temp_list.append(jetson.temperature['CPU']['temp'])
        board_temp_list.append(jetson.temperature['Tboard']['temp'])
        perf_list.append(0)
        
        #incrémentation du nombre de valeurs ajoutées
        value_counts += 1


perf_list[0] = input("entrer valeur de perf : ")
donnees = list(zip(power_tot_list, power_tot_avg_list, ram_list, gpu_temp_list, cpu_temp_list, board_temp_list, perf_list))

#ecriture des data dans un fichier csv
file_name = input("\nentrer un nom de fichier : ") + ".csv"
with open(file_name, 'w', encoding='UTF8', newline='') as csvfile:
	
    writer = csv.DictWriter(csvfile, fieldnames=entetes)
    writer.writeheader()
	
    for donnee in donnees: 
        writer.writerow({'puissance tot' : donnee[0], 'puissance tot moy': donnee[1], 'ram used' : donnee[2], 'gpu temp' : donnee[3], 'cpu temp' : donnee[4], 'board temp' : donnee[5],'perf': donnee[6]})

file_path = os.path.join(os.getcwd(), file_name)
print("file saved in : ", file_path)