import numpy as np
import parameter_fitness as pf
import parameter_fitness_bass as pfb
def sum_fitness_birama(fitness_birama_all, banyak_birama):
    sum_fitness_birama_list = []
    for i in range(banyak_birama):
        sum_fitness_birama_list.append(sum(fitness_birama_all[i]))
    return sum_fitness_birama_list

def sum_fitness_birama_all(sum_fitness_birama):
    return sum(sum_fitness_birama)

# arr = [[3, 9, 2, 10], [0, 12, 4, 6], [5, 5, 13, 12], [7, 1, [0, 10], 1], [5, [6, 11, 7, 4], 11, 3]]
# arr2 = [[13, 10, 6, 7], [[8, 0, 7, 5], [13, 3, 9, 0], [3, 2], [9, 5, 10, 0]], [[10, 0, 8, 12], 9, 12, 14], [11, 2, 13, 13], [7, [9, 10, 4, 2], 3, [1,2]]]
# arr3 = [[10, [2, 10, 3, 6], 6, 13], [8, 6, 7, [13, 1]], [10, [0, 12], 7, 15], [2, 15, 15, [8, 0, 5, 3]], [4, 0, [8, 5, 10, 11], 5]]
# arr4 = [[1, [8, 3], 10, 8], [9, 2, 7, 7], [4, 9, 6, 12], [4, [8, 11], 3, 3], [0, 4, 3, 4]]

# print(interval_sum(arr4,5,4,15))

def mean_interval_birama(komposisi, banyak_birama, anggota_birama, range_nada):
    mean_interval_list = []
    konversi_komposisi = pf.komposisi_convert(komposisi, banyak_birama, anggota_birama, range_nada)
    interval = pf.hitung_interval(konversi_komposisi,banyak_birama,anggota_birama,"interval_sum")

    for i in range(len(interval)):
        sum_list = 0
        for j in range(len(interval[i])):
            sum_list += interval[i][j]
        mean_interval_list.append(sum_list/len(interval[i]))
    return mean_interval_list
# arr = [[6, 7, 8], [12, 8, 2], [0, 8, 1], [6, 1, 10, 9], [1, 5, 4, 3, 7, 8]]
# arr = [[3, 9, 2, 10], [0, 12, 4, 6], [5, 15, 13, 12], [7, 1, [0, 10], 1], [5, [6, 11, 7, 4], 11, 3]]
# arr = [[[3, 9, 2, 10], [0, 12, 4, 6], [5, 15, 13, 12], [7, 1, [0, 10], 1], [5, [6, 11, 7, 4], 11, 3]], [[10, 4, 13, 9], [2, 1, 8, 3], [7, [0, 3, 12, 10], 1, 9], [5, 12, 4, 9], [8, 8, 8, 0]], [[5, 13, 7, 1], [13, 4, [4, 5, 7, 6], 2], [10, 5, 14, 0], [4, 5, 4, 2], [10, 13, [9, 4, 13, 2], 1]], [[8, 11, 2, [6, 2]], [11, 0, 6, 14], [[4, 7, 12, 1], 0, 1, 9], [7, 3, [3, 10], [13, 0]], [7, 8, [1, 12], 0]], [[9, 8, 4, 10], [[7, 8, 1, 11], 14, 11, 9], [[10, 9], 0, 4, 4], [7, 6, 9, 9], [0, 3, 2, 7]]]
# print(mean_interval_birama(arr,5,4,15))

def mean_interval_birama_bass(komposisi, anggota_birama):
    interval = pfb.hitung_interval_bass(komposisi, anggota_birama, "interval_sum")
    sum_list = 0
    for i in range(len(interval)):
        sum_list += interval[i]

    return sum_list/len(interval)

def varian_interval_birama(komposisi, banyak_birama, anggota_birama, range_nada, mean_interval_list):
    varian_interval_list = []
    konversi_komposisi = pf.komposisi_convert(komposisi, banyak_birama, anggota_birama, range_nada)
    interval = pf.hitung_interval(konversi_komposisi,banyak_birama,anggota_birama,"interval_sum")
    for i in range(len(interval)):
        square_difference = []
        for j in range(len(interval[i])):
            square_difference.append(pow(interval[i][j]-mean_interval_list[i],2))
        # varian_interval_birama_list.append(sum(square_difference)/len(interval[i]))
        varian_interval_list.append(sum(square_difference)/len(interval[i]))
    
    return np.array(varian_interval_list)

def varian_interval_birama_bass(komposisi, anggota_birama, mean_interval_list):
    interval = pfb.hitung_interval_bass(komposisi, anggota_birama, "interval_sum")
    square_difference = []
    for i in range(len(interval)):
        square_difference.append(pow(interval[i]-mean_interval_list,2))

    return sum(square_difference)/len(interval)
# arr_b = [[1, 8, 5, 6, 5], [2, 5, 3, 3, 8], [3, 4, 4, 1, 7], [7, 8, 5, 7, 7], [2, 7, 3, 7, 3]]
# for i in range(len(arr_b)):
#     print(varian_interval_birama_bass(arr_b[i],5,mean_interval_birama_bass(arr_b[i],5)))

# arr = [[6, 7, 8], [12, 8, 2], [0, 8, 1], [6, 1, 10, 9], [1, 5, 4, 3, 7, 8]]
# arr = [[3, 9, 2, 10], [0, 12, 4, 6], [5, 15, 13, 12], [7, 1, [0, 10], 1], [5, [6, 11, 7, 4], 11, 3]]
# arr = [[[3, 9, 2, 10], [0, 12, 4, 6], [5, 15, 13, 12], [7, 1, [0, 10], 1], [5, [6, 11, 7, 4], 11, 3]], [[10, 4, 13, 9], [2, 1, 8, 3], [7, [0, 3, 12, 10], 1, 9], [5, 12, 4, 9], [8, 8, 8, 0]], [[5, 13, 7, 1], [13, 4, [4, 5, 7, 6], 2], [10, 5, 14, 0], [4, 5, 4, 2], [10, 13, [9, 4, 13, 2], 1]], [[8, 11, 2, [6, 2]], [11, 0, 6, 14], [[4, 7, 12, 1], 0, 1, 9], [7, 3, [3, 10], [13, 0]], [7, 8, [1, 12], 0]], [[9, 8, 4, 10], [[7, 8, 1, 11], 14, 11, 9], [[10, 9], 0, 4, 4], [7, 6, 9, 9], [0, 3, 2, 7]]]
# print(mean_interval_birama(arr,5,4,15))
# for i in range(len(arr)):
#     print(varian_interval_birama(arr[i], 5, 4, 15, mean_interval_birama(arr[i],5,4,15)))

def sum_mean_interval_birama(mean_interval_birama):
    return np.sum(mean_interval_birama)

def sum_varian_interval_birama(varian_interval_birama):
    return np.sum(varian_interval_birama)

def total_fitness(sum_mean_interval_birama,sum_varian_interval_birama,sum_fitness_birama_all):
    return np.sum([sum_mean_interval_birama,sum_varian_interval_birama,sum_fitness_birama_all])