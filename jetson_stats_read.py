from jtop import jtop 
import csv
import os

#declaration des listes contenant les données
power_list = []
ram_list = []
gpu_temp_list = []
cpu_temp_list = []
board_temp_list = []
perf_list = []
entetes = ['puissance tot', 'ram used', 'gpu temp', 'cpu temp', 'board temp', 'perf']

with jtop() as jetson:
    # jetson.ok() will provide the proper update frequency
    while jetson.ok():
        os.system('clear')
        print("running...")

        # lit et affiche les stats de la jetson
        print("puissance totale : ", int(jetson.power['tot']['power'])/1000, "W")
        print("fréquence gpu : ", int(jetson.gpu['ga10b']['freq']['cur'])/1000, "MHz")
        print("temperature gpu : ", jetson.temperature['GPU']['temp'], "°C")
        print("temperature cpu : ", jetson.temperature['CPU']['temp'], "°C")
        print("temperature carte : ",jetson.temperature['Tboard']['temp'], "°C")
        print("ram used : ", round(jetson.memory['RAM']['used']/jetson.memory['RAM']['tot']*100,2), "%")
        
        #ajout des stats aux listes
        power_list.append(jetson.power['tot']['power'])
        ram_list.append(round(jetson.memory['RAM']['used']/jetson.memory['RAM']['tot']*100,1))
        gpu_temp_list.append(jetson.temperature['GPU']['temp'])
        cpu_temp_list.append(jetson.temperature['CPU']['temp'])
        board_temp_list.append(jetson.temperature['Tboard']['temp'])
        perf_list.append(0)
        
perf_list[0]= input("entrer valeur de perf : ")
donnees = list(zip(power_list, ram_list, gpu_temp_list, cpu_temp_list, board_temp_list, perf_list))

#ecriture des data dans un fichier csv
with open(input("\nentrer un nom de fichier : ") + ".csv", 'w', encoding='UTF8', newline='') as csvfile:
	
    writer = csv.DictWriter(csvfile, fieldnames=entetes)
    writer.writeheader()
	
    for donnee in donnees:
        writer.writerow({'puissance tot' : donnee[0], 'ram used' : donnee[1], 'gpu temp' : donnee[2], 'cpu temp' : donnee[3], 'board temp' : donnee[4],'perf': donnee[5]})

