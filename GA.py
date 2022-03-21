import numpy as np
import parameter_fitness as pf
import random

def inisialisasi_individu(banyak_birama, anggota_birama, range_nada, komposisi):
    alt_nums_core = []
    for i in range(banyak_birama):
        alt_nums = []
        randnums = []
        sama = -1
        for j in range(anggota_birama):
            num = random.randint(0,range_nada-1)
            alt_nums.append(num)
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
        alt_nums_core.append(alt_nums)
        komposisi[i] = np.array(randnums)

    return komposisi, np.array(alt_nums_core)

def seleksi_turnamen(fitness_individu_list, peserta_turnamen, jumlah_turnamen):
    hasil_seleksi_list = []
    for i in range(jumlah_turnamen):
        current_turnamen = []
        current_turnamen = random.sample(fitness_individu_list, peserta_turnamen)
        hasil_seleksi_list.append(max(current_turnamen))
    return hasil_seleksi_list

def mutasi(komposisi, anggota_birama, probabilitas_mutasi, range_nada):
    operasi = ["+","-"]
    mengubah_nada = [1,2,3,4,5,6]
    for i in range(len(komposisi)):
        stop_mutasi = 0
        while stop_mutasi < int(anggota_birama*probabilitas_mutasi):
            kena_mutasi = random.randint(0,anggota_birama-1)
            if komposisi[i][kena_mutasi] != range_nada:
                pilih_operasi = random.choice(operasi)
                if pilih_operasi == "+" and komposisi[i][kena_mutasi] + 7 < range_nada:
                    komposisi[i][kena_mutasi] += 7
                    stop_mutasi += 1
                elif komposisi[i][kena_mutasi]-7 > 0:
                    komposisi[i][kena_mutasi] -= 7
                    stop_mutasi += 1
    
        stop_mutasi = 0
        while stop_mutasi < int(anggota_birama*probabilitas_mutasi):
            kena_mutasi = random.randint(0,anggota_birama-1)
            if komposisi[i][kena_mutasi] != range_nada:
                pilih_operasi = random.choice(operasi)
                pilih_mengubah_nada = random.choice(mengubah_nada)
                if pilih_operasi == "+" and komposisi[i][kena_mutasi] + pilih_mengubah_nada < range_nada:
                    komposisi[i][kena_mutasi] += pilih_mengubah_nada
                    stop_mutasi += 1
                elif komposisi[i][kena_mutasi]-pilih_mengubah_nada > 0:
                    komposisi[i][kena_mutasi] -= pilih_mengubah_nada
                    stop_mutasi += 1

        stop_mutasi = 0
        while stop_mutasi < int(anggota_birama*probabilitas_mutasi):
            kena_mutasi = random.randint(0,anggota_birama-1)
            kena_mutasi_sec = random.randint(0,anggota_birama-1)
            if komposisi[i][kena_mutasi] != range_nada and komposisi[i][kena_mutasi_sec] != range_nada:
                komposisi[i][kena_mutasi], komposisi[i][kena_mutasi_sec] = komposisi[i][kena_mutasi_sec], komposisi[i][kena_mutasi]
                stop_mutasi += 1


    return komposisi