import numpy as np
import random
import GA
from individu import individu_object
import parameter_fitness as pf
import fungsi_fitness as ff

banyak_birama = int(input("Banyak birama: "))
banyak_individu = int(input("Banyak individu: "))
probabilitas_mutasi = int(input("Probabilitas mutasi: "))/100
range_nada = 14+1
anggota_birama = 10
komposisi = np.empty((banyak_birama,anggota_birama))

def generate_populasi(banyak_birama, anggota_birama, range_nada, komposisi, banyak_individu):
    komposisi_individu_list = []
    komposisi_alt_individu_list = []
    for i in range(banyak_individu):
        populasi_awal = GA.inisialisasi_individu(banyak_birama, anggota_birama, range_nada, komposisi)
        alt_populasi = populasi_awal[1]
        populasi_awal = populasi_awal[0]
        komposisi_individu_list.append(populasi_awal)
        komposisi_alt_individu_list.append(alt_populasi)
        komposisi = np.empty((banyak_birama,anggota_birama))
    return komposisi_individu_list, komposisi_alt_individu_list

# print(generate_populasi(banyak_birama, anggota_birama, range_nada, komposisi, banyak_individu))
populasi_awal = generate_populasi(banyak_birama, anggota_birama, range_nada, komposisi, banyak_individu)
alt_populasi = populasi_awal[1]
populasi_awal = populasi_awal[0]
print(populasi_awal)

def hitung_fitness(populasi_awal, alt_populasi, range_nada, banyak_birama, anggota_birama, banyak_individu):
    total_fitness_list = []
    for i in range(len(populasi_awal)):
        variasi_nada_list = pf.variasi_nada(populasi_awal[i], range_nada, banyak_birama)
        interval_disonan_list = pf.interval_disonan(populasi_awal[i],anggota_birama,range_nada)
        arah_kontur_list = pf.arah_kontur(populasi_awal[i],anggota_birama)
        stabilitas_kontur_list = pf.stabilitas_kontur(alt_populasi[i], anggota_birama)
        variasi_irama_list = pf.variasi_irama(populasi_awal[i],anggota_birama,range_nada)
        rentang_irama_list = pf.rentang_irama(populasi_awal[i],anggota_birama,range_nada)
        
        fitness_birama_all = []
        for j in range(banyak_birama):
            fitness_birama = [variasi_nada_list[j],interval_disonan_list[j],arah_kontur_list[j],stabilitas_kontur_list[j],variasi_irama_list[j],rentang_irama_list[j]]
            fitness_birama_all.append(fitness_birama)
        sum_fitness_birama = ff.sum_fitness_birama(fitness_birama_all, banyak_birama)
        sum_fitness_birama_all = ff.sum_fitness_birama_all(sum_fitness_birama)
        interval_sum_list = ff.interval_sum(populasi_awal[i], anggota_birama)
        mean_interval_birama = ff.mean_interval_birama(interval_sum_list, anggota_birama)
        varian_interval_birama = ff.varian_interval_birama(interval_sum_list, mean_interval_birama, anggota_birama)
        sum_mean_interval_birama = ff.sum_mean_interval_birama(mean_interval_birama)
        sum_varian_interval_birama = ff.sum_varian_interval_birama(varian_interval_birama)
        total_fitness = ff.total_fitness(sum_mean_interval_birama,sum_varian_interval_birama,sum_fitness_birama_all)
        total_fitness_list.append(total_fitness)
    
    return total_fitness_list

total_fitness_list = hitung_fitness(populasi_awal, alt_populasi, range_nada, banyak_birama, anggota_birama, banyak_individu)
print("Total fitness: " , total_fitness_list)

def update_generasi(populasi_awal, total_fitness_list, banyak_individu):
    fitness_dict = {}
    for i, val in enumerate(total_fitness_list):
        fitness_dict[val] = i
    next_gen_list = []
    hasil_seleksi = GA.seleksi_turnamen(total_fitness_list, 3, banyak_individu)
    for val in hasil_seleksi:
        next_gen_list.append(populasi_awal[fitness_dict[val]])
    return next_gen_list

# print(update_generasi(populasi_awal, total_fitness_list, banyak_individu))

def mutasi_generasi(populasi_awal, anggota_birama, probabilitas_mutasi, range_nada, banyak_individu):
    individu_mutasi_list = []
    for i in range(banyak_individu):
        individu_mutasi_list.append(GA.mutasi(populasi_awal[i], anggota_birama, probabilitas_mutasi, range_nada))

    return individu_mutasi_list
print("Hasil Mutasi: ")
print(mutasi_generasi(populasi_awal, anggota_birama, probabilitas_mutasi, range_nada, banyak_individu))  

