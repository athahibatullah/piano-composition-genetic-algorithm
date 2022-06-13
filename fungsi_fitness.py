import numpy as np
import parameter_fitness as pf
def sum_fitness_birama(fitness_birama_all, banyak_birama):
    sum_fitness_birama_list = []
    for i in range(banyak_birama):
        sum_fitness_birama_list.append(sum(fitness_birama_all[i]))
    return sum_fitness_birama_list

def sum_fitness_birama_all(sum_fitness_birama):
    return sum(sum_fitness_birama)

def interval_sum(komposisi, banyak_birama, anggota_birama, range_nada):
    interval_sum_list = []
    konversi_komposisi = pf.komposisi_convert(komposisi, banyak_birama, anggota_birama, range_nada)
    interval = pf.hitung_interval(konversi_komposisi,banyak_birama,anggota_birama,"interval_sum")
    for i in range(banyak_birama):
        interval_sum = 0
        for j in range(len(interval[i])):
            interval_sum += interval[i][j]
        interval_sum_list.append(interval_sum)
    return np.array(interval_sum_list)

# arr = [[3, 9, 2, 10], [0, 12, 4, 6], [5, 5, 13, 12], [7, 1, [0, 10], 1], [5, [6, 11, 7, 4], 11, 3]]
# arr2 = [[13, 10, 6, 7], [[8, 0, 7, 5], [13, 3, 9, 0], [3, 2], [9, 5, 10, 0]], [[10, 0, 8, 12], 9, 12, 14], [11, 2, 13, 13], [7, [9, 10, 4, 2], 3, [1,2]]]
# arr3 = [[10, [2, 10, 3, 6], 6, 13], [8, 6, 7, [13, 1]], [10, [0, 12], 7, 15], [2, 15, 15, [8, 0, 5, 3]], [4, 0, [8, 5, 10, 11], 5]]
# arr4 = [[1, [8, 3], 10, 8], [9, 2, 7, 7], [4, 9, 6, 12], [4, [8, 11], 3, 3], [0, 4, 3, 4]]

# print(interval_sum(arr4,5,4,15))

def interval_sum_bass(komposisi, anggota_birama):
    interval_sum_list = []
    interval = 0
    for i in range(anggota_birama-1):
        interval += abs(komposisi[i] - komposisi[i+1])
    interval_sum_list.append(interval)
    return np.array(interval_sum_list)

def mean_interval_birama(interval_sum_list, anggota_birama):
    mean_interval_list = []
    for i in range(len(interval_sum_list)):
        mean_interval_list.append(interval_sum_list[i]/anggota_birama)
    return np.array(mean_interval_list)

def varian_interval_birama(interval_sum_list, mean_interval_list, anggota_birama):
    varian_interval_list = []
    for i in range(len(mean_interval_list)):
        varian_interval_list.append(pow(interval_sum_list[i]-mean_interval_list[i],2)/anggota_birama)
    return np.array(varian_interval_list)

def sum_mean_interval_birama(mean_interval_birama):
    return np.sum(mean_interval_birama)

def sum_varian_interval_birama(varian_interval_birama):
    return np.sum(varian_interval_birama)

def total_fitness(sum_mean_interval_birama,sum_varian_interval_birama,sum_fitness_birama_all):
    return np.sum([sum_mean_interval_birama,sum_varian_interval_birama,sum_fitness_birama_all])