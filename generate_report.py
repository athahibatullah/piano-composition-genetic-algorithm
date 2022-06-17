import csv

def generate_csv(populasi_awal, populasi_treble, populasi_bass, fitness_treble, fitness_bass):
    with open('report/hasil.csv', 'w', newline='') as csvfile:
        fieldnames = ['No.', 'Individu Treble', 'Individu Bass', 'Fitness Treble', 'Fitness Bass']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(len(populasi_treble)):
            writer.writerow({'No.' : i+1, 'Individu Treble': populasi_treble[i], 'Individu Bass': populasi_bass[i], 'Fitness Treble': fitness_treble[i], 'Fitness Bass': fitness_bass[i]})

def proses_fitness(fitness_treble, fitness_bass):
    fieldnames = ['Generasi ke-']
    row = {}
    for i in range(len(fitness_treble[0])):
        individu_ke = "Individu " + str(i+1)
        fieldnames.append(individu_ke)
    # row[fieldnames[0]] = "1"
    # row[fieldnames[1]] = fitness_treble[0][0]
    # row[fieldnames[2]] = fitness_treble[1][0]
    with open('report/proses_fitness.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(fitness_treble)):
            row[fieldnames[0]] = i+1
            for j in range(len(fitness_treble[i])):
                row[fieldnames[j+1]] = fitness_treble[i][j]
            writer.writerow(row)

#{'No.': i+1, 'generasi 1': fitness_treble[i][j], 'generasi 2': fitness_treble[i+1][j]}
    # with open('report/proses_fitness.csv', 'w', newline='') as csvfile:
    #     fieldnames = ['No.', 'Individu Treble', 'Individu Bass', 'Fitness Treble', 'Fitness Bass']
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #     writer.writeheader()
    #     for i in range(len(populasi_treble)):
    #         writer.writerow({'No.' : i+1, 'Individu Treble': populasi_treble[i], 'Individu Bass': populasi_bass[i], 'Fitness Treble': fitness_treble[i], 'Fitness Bass': fitness_bass[i]})

# arr = [[49.55825822966912, 58.34241004093945, 74.6214133089133, 82.94163475413475, 79.8252312108695], [64.66668652884405, 97.2653785103785, 55.15297056744426, 83.43595764582003, 49.265584723918046]]
# print(proses_fitness(arr,arr))