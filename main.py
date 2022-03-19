import numpy as np
import random
import GA
import parameter_fitness as pf
import fungsi_fitness as ff

banyak_birama = int(input())
range_nada = 14+1
anggota_birama = 10
komposisi = np.empty((banyak_birama,anggota_birama))

populasi_awal = GA.inisialisasi_individu(banyak_birama, anggota_birama, range_nada, komposisi)
alt_populasi = populasi_awal[1]
populasi_awal = populasi_awal[0]

print(populasi_awal)

variasi_nada_list = pf.variasi_nada(populasi_awal, range_nada, banyak_birama)
interval_disonan_list = pf.interval_disonan(populasi_awal,anggota_birama,range_nada)
arah_kontur_list = pf.arah_kontur(populasi_awal,anggota_birama)
stabilitas_kontur_list = pf.stabilitas_kontur(alt_populasi, anggota_birama)
variasi_irama_list = pf.variasi_irama(populasi_awal,anggota_birama,range_nada)
rentang_irama_list = pf.rentang_irama(populasi_awal,anggota_birama,range_nada)

fitness_birama_all = []

for i in range(banyak_birama):
    fitness_birama = [variasi_nada_list[i],interval_disonan_list[i],arah_kontur_list[i],stabilitas_kontur_list[i],variasi_irama_list[i],rentang_irama_list[i]]
    fitness_birama_all.append(fitness_birama)

# print(fitness_birama_all)
# print(pf.variasi_nada(populasi_awal, range_nada, banyak_birama))
# print(pf.interval_disonan(populasi_awal,anggota_birama,range_nada))
# print(pf.arah_kontur(populasi_awal,anggota_birama))
# print(pf.variasi_irama(populasi_awal,anggota_birama,range_nada))
# print(pf.rentang_irama(populasi_awal,anggota_birama,range_nada))
sum_fitness_birama = ff.sum_fitness_birama(fitness_birama_all, banyak_birama)
sum_fitness_birama_all = ff.sum_fitness_birama_all(sum_fitness_birama)

# print(sum_fitness_birama,sum_fitness_birama_all)
interval_sum_list = ff.interval_sum(populasi_awal, anggota_birama)
mean_interval_birama = ff.mean_interval_birama(interval_sum_list, anggota_birama)
varian_interval_birama = ff.varian_interval_birama(interval_sum_list, mean_interval_birama, anggota_birama)
sum_mean_interval_birama = ff.sum_mean_interval_birama(mean_interval_birama)
sum_varian_interval_birama = ff.sum_varian_interval_birama(varian_interval_birama)

# print(sum_mean_interval_birama,sum_varian_interval_birama)

total_fitness = ff.total_fitness(sum_mean_interval_birama,sum_varian_interval_birama,sum_fitness_birama_all)
print(total_fitness)