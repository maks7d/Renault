import csv

with open(input('nom du fichier : ') + ".csv", 'r', newline='') as csvfile:

    reader = csv.DictReader(csvfile)

    for row in reader:
        puissance_tot = row['puissance tot']
        gpu_freq = row['gpu freq']

        print(f" puissance totale : {puissance_tot} ")
        print(f"gpu freq : {gpu_freq}")