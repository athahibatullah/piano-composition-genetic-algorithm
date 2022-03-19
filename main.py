import numpy as np
import random
import GA
import parameter_fitness as pf
import fungsi_fitness as ff

banyak_birama = int(input())
range_nada = 14+1
anggota_birama = 10
komposisi = np.empty((banyak_birama,anggota_birama))

# print(GA.inisialisasi_individu(banyak_birama, range_nada, komposisi))
populasi_awal = GA.inisialisasi_individu(banyak_birama, anggota_birama, range_nada, komposisi)

print(pf.variasi_nada(populasi_awal, range_nada, banyak_birama))
print(pf.interval_disonan(populasi_awal,anggota_birama,range_nada))
print(pf.arah_kontur(populasi_awal,anggota_birama))
print(pf.variasi_irama(populasi_awal,anggota_birama,range_nada))
print(pf.rentang_irama(populasi_awal,anggota_birama,range_nada))