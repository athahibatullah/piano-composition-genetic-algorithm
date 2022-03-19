def sum_fitness_birama(fitness_birama_all, banyak_birama):
    sum_fitness_birama_list = []
    for i in range(banyak_birama):
        sum_fitness_birama_list.append(sum(fitness_birama_all[i]))

    return sum_fitness_birama_list

def sum_fitness_birama_all(sum_fitness_birama):
    return sum(sum_fitness_birama)

def interval_sum(komposisi, anggota_birama):
    interval_sum_list = []
    for i in range(len(komposisi)):
        interval = 0
        for j in range(anggota_birama-1):
            interval += abs(komposisi[i][j] - komposisi[i][j+1])
        interval_sum_list.append(interval)
    return interval_sum_list

def mean_interval_birama(interval_sum_list, anggota_birama):
    mean_interval_list = []
    for i in range(len(interval_sum_list)):
        mean_interval_list.append(interval_sum_list[i]/anggota_birama)
    return mean_interval_list

def varian_interval_birama(interval_sum_list, mean_interval_list, anggota_birama):
    varian_interval_list = []
    for i in range(len(mean_interval_list)):
        varian_interval_list.append(pow(interval_sum_list[i]-mean_interval_list[i],2)/anggota_birama)
    return varian_interval_list

def sum_mean_interval_birama(mean_interval_birama):
    return sum(mean_interval_birama)

def sum_varian_interval_birama(varian_interval_birama):
    return sum(varian_interval_birama)

def total_fitness(sum_mean_interval_birama,sum_varian_interval_birama,sum_fitness_birama_all):
    return sum([sum_mean_interval_birama,sum_varian_interval_birama,sum_fitness_birama_all])