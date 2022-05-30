import numpy as np
import parameter_fitness as pf
import random

def inisialisasi_individu(banyak_birama, anggota_birama, range_nada, komposisi):
    for i in range(banyak_birama):
        randnums = []
        sama = -1
        for j in range(anggota_birama):
            num = random.randint(0,range_nada-1)
            if j == 0:
                randnums.append(num)
            elif randnums[j-1] == num:
                randnums.append(range_nada)
                sama = num
            elif num == sama:
                randnums.append(range_nada)
            elif num != sama:
                randnums.append(num)
                sama = -1
            else:
                randnums.append(num)
        # quota = 15
        # while quota > 0:
        #     if quota == 15:
        #         num = random.randint(0,14)
        #     else:
        #         num = random.randint(0,15)

        #     if num == 15:
        #         banyak_random = random.randint(1,quota) 
        #         for j in range(banyak_random):
        #             randnums.append(15)
        #         quota -= banyak_random
        #     else:
        #         randnums.append(num)
        #         quota -= 1
        komposisi[i] = np.array(randnums)

    return komposisi

def seleksi_turnamen(fitness_individu_list, peserta_turnamen, jumlah_turnamen):
    hasil_seleksi_list = []
    for i in range(jumlah_turnamen):
        current_turnamen = []
        current_turnamen = random.sample(fitness_individu_list, peserta_turnamen)
        hasil_seleksi_list.append(max(current_turnamen))
    
    return hasil_seleksi_list

def mutasi(komposisi, banyak_birama, anggota_birama, probabilitas_mutasi, range_nada):
    operasi = ["+","-"]
    mengubah_nada = [1,2,3,4,5,6]
    # for i in range(len(komposisi)):
    stop_mutasi = 0
    # print(int(anggota_birama*probabilitas_mutasi*banyak_birama))
    while stop_mutasi < int(anggota_birama*probabilitas_mutasi*banyak_birama):
        kena_mutasi_i = random.randint(0,banyak_birama-1)
        kena_mutasi_j = random.randint(0,anggota_birama-1)
        if komposisi[kena_mutasi_i][kena_mutasi_j] != range_nada:
            pilih_operasi = random.choice(operasi)
            if pilih_operasi == "+" and komposisi[kena_mutasi_i][kena_mutasi_j] + 7 < range_nada:
                komposisi[kena_mutasi_i][kena_mutasi_j] += 7
                stop_mutasi += 1
            elif komposisi[kena_mutasi_i][kena_mutasi_j]-7 > 0:
                komposisi[kena_mutasi_i][kena_mutasi_j] -= 7
                stop_mutasi += 1

    stop_mutasi = 0
    while stop_mutasi < int(anggota_birama*probabilitas_mutasi*banyak_birama):
        kena_mutasi_i = random.randint(0,banyak_birama-1)
        kena_mutasi_j = random.randint(0,anggota_birama-1)
        if komposisi[kena_mutasi_i][kena_mutasi_j] != range_nada:
            pilih_operasi = random.choice(operasi)
            pilih_mengubah_nada = random.choice(mengubah_nada)
            if pilih_operasi == "+" and komposisi[kena_mutasi_i][kena_mutasi_j] + pilih_mengubah_nada < range_nada:
                komposisi[kena_mutasi_i][kena_mutasi_j] += pilih_mengubah_nada
                stop_mutasi += 1
            elif komposisi[kena_mutasi_i][kena_mutasi_j]-pilih_mengubah_nada > 0:
                komposisi[kena_mutasi_i][kena_mutasi_j] -= pilih_mengubah_nada
                stop_mutasi += 1

    stop_mutasi = 0
    while stop_mutasi < int(anggota_birama*probabilitas_mutasi*banyak_birama):
        kena_mutasi_i = random.randint(0,banyak_birama-1)
        kena_mutasi_j = random.randint(0,anggota_birama-1)
        kena_mutasi_i_sec = random.randint(0,banyak_birama-1)
        kena_mutasi_j_sec = random.randint(0,anggota_birama-1)
        if komposisi[kena_mutasi_i][kena_mutasi_j] != range_nada and komposisi[kena_mutasi_i_sec][kena_mutasi_j_sec] != range_nada:
            komposisi[kena_mutasi_i][kena_mutasi_j], komposisi[kena_mutasi_i_sec][kena_mutasi_j_sec] = komposisi[kena_mutasi_i_sec][kena_mutasi_j_sec], komposisi[kena_mutasi_i][kena_mutasi_j]
            stop_mutasi += 1


    return komposisi