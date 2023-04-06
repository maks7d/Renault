from jtop import jtop 
import csv

#declaration des listes contenant les données
power_list = []
gpu_freq_list = []
#data_list = [power_list, gpu_freq_list]
entetes = ['puissance tot', 'gpu freq']



with jtop() as jetson:
    # jetson.ok() will provide the proper update frequency
    while jetson.ok():
        # lit et affiche les stats de la jetson
        print("puissance totale : ", int(jetson.power['tot']['power'])/1000, "W")
        print("fréquence gpu : ", int(jetson.gpu['ga10b']['freq']['cur'])/1000, "MHz")

        #ajout des stats aux listes
        power_list.append(jetson.power['tot']['power'])
        gpu_freq_list.append(jetson.gpu['ga10b']['freq']['cur'])

donnees = list(zip(power_list, gpu_freq_list))

#ecriture des data dans un fichier csv
with open(input("\nentrer un nom de fichier : ") + ".csv", 'w', encoding='UTF8', newline='') as csvfile:
	
    writer = csv.DictWriter(csvfile, fieldnames=entetes)
    writer.writeheader()
	
    for donnee in donnees:
        writer.writerow({'puissance tot' : donnee[0], 'gpu freq' : donnee[1]})
