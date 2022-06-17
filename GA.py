import random

def inisialisasi_individu(banyak_birama, anggota_birama, range_nada, komposisi):
    for i in range(banyak_birama):
        randnums= []
        sama = -1
        for j in range(anggota_birama):
            num = random.randint(0,range_nada+1)
            if num == range_nada: #anggap 16
                random_arr = random.sample(range(0, range_nada-1), 2)
                randnums.append(random_arr)
            elif num == range_nada+1: #anggap 17
                random_arr = random.sample(range(0, range_nada-1), 4)
                randnums.append(random_arr)
            else:
                if j == 0:
                    randnums.append(num)
                elif not isinstance(randnums[j-1], list) and randnums[j-1] == num:
                    randnums.append(range_nada)
                    sama = num
                elif num == sama:
                    randnums.append(range_nada)
                elif num != sama:
                    randnums.append(num)
                    sama = -1
                else:
                    randnums.append(num)
        komposisi.append(randnums)

    return komposisi

# print(inisialisasi_individu(5,4,15,[]))

def inisialisasi_bass(banyak_birama, anggota_birama, range_nada, komposisi):
    randnums= []
    for i in range(anggota_birama):
        # random_number =  random.randint(1,range_nada-2)
        random_number =  random.randint(1,8)
        randnums.append(random_number)
    komposisi = randnums
    return komposisi

def seleksi_turnamen(fitness_individu_list, peserta_turnamen, jumlah_turnamen):
    hasil_seleksi_list = []
    for i in range(jumlah_turnamen):
        current_turnamen = []
        current_turnamen = random.sample(fitness_individu_list, peserta_turnamen)
        hasil_seleksi_list.append(max(current_turnamen))
    
    return hasil_seleksi_list

def change_durasi(komposisi, banyak_birama, anggota_birama, range_nada):
    for i in range(banyak_birama):
        for j in range(anggota_birama):
            if not isinstance(komposisi[i][j], list):
                if komposisi[i][j] == 16:
                    komposisi[i][j] = random.sample(range(0, range_nada-1), 2)
                elif komposisi[i][j] == 17:
                    komposisi[i][j] = random.sample(range(0, range_nada-1), 4)
    
    return komposisi

def mutasi(komposisi, banyak_birama, anggota_birama, probabilitas_mutasi, range_nada):
    operasi = ["+","-"]
    mengubah_nada = [1,2,3,4,5,6]
    stop_mutasi = 0
    while stop_mutasi < int(anggota_birama*probabilitas_mutasi*banyak_birama):
        kena_mutasi_i = random.randint(0,banyak_birama-1)
        kena_mutasi_j = random.randint(0,anggota_birama-1)
        pilih_operasi = random.choice(operasi)
        kena_mutasi = komposisi[kena_mutasi_i][kena_mutasi_j]
        if isinstance(kena_mutasi, list):
            ubah = [False, True]
            ubah_durasi = random.choices(ubah, weights=[0.9,0.1])
            k = random.randint(0,len(kena_mutasi)-1)
            if ubah_durasi:
                ubah_random = random.randint(0,range_nada+2)
                if pilih_operasi == "+" and ubah_random + 7 <= range_nada:
                    if ubah_random + 7 == 15 and k == 0:
                        continue
                    else:
                        kena_mutasi = ubah_random
                        kena_mutasi += 7
                        stop_mutasi += 1
                elif ubah_random-7 >= 0:
                    kena_mutasi = ubah_random
                    kena_mutasi -= 7
                    stop_mutasi += 1
                komposisi[kena_mutasi_i][kena_mutasi_j] = kena_mutasi
            else:
                if pilih_operasi == "+" and kena_mutasi[k] + 7 <= range_nada:
                    if kena_mutasi[k] + 7 == 15 and k == 0:
                        continue
                    else:    
                        kena_mutasi[k] += 7
                        stop_mutasi += 1
                elif kena_mutasi[k]-7 >= 0:
                    kena_mutasi[k] -= 7
                    stop_mutasi += 1
                komposisi[kena_mutasi_i][kena_mutasi_j][k] = kena_mutasi[k]

        else:
            if pilih_operasi == "+" and kena_mutasi + 7 <= range_nada+2:
                if kena_mutasi + 7 == 15 and kena_mutasi_j == 0:
                    continue
                else:
                    kena_mutasi += 7
                    stop_mutasi += 1
            elif kena_mutasi-7 >= 0:
                kena_mutasi -= 7
                stop_mutasi += 1
            komposisi[kena_mutasi_i][kena_mutasi_j] = kena_mutasi
    # print(kena_mutasi_i,kena_mutasi_j)
    komposisi = change_durasi(komposisi, banyak_birama, anggota_birama, range_nada)

    stop_mutasi = 0
    while stop_mutasi < int(anggota_birama*probabilitas_mutasi*banyak_birama):
        kena_mutasi_i = random.randint(0,banyak_birama-1)
        kena_mutasi_j = random.randint(0,anggota_birama-1)
        pilih_operasi = random.choice(operasi)
        kena_mutasi = komposisi[kena_mutasi_i][kena_mutasi_j]
        pilih_mengubah_nada = random.choice(mengubah_nada)
        if isinstance(kena_mutasi, list):
            ubah = [False, True]
            ubah_durasi = random.choices(ubah, weights=[0.9,0.1])
            k = random.randint(0,len(kena_mutasi)-1)
            if ubah_durasi:
                    ubah_random = random.randint(0,range_nada+2)
                    if pilih_operasi == "+" and ubah_random + pilih_mengubah_nada <= range_nada:
                        if ubah_random + pilih_mengubah_nada == 15 and k == 0:
                            continue
                        else:
                            kena_mutasi = ubah_random
                            kena_mutasi += pilih_mengubah_nada
                            stop_mutasi += 1
                    elif ubah_random-pilih_mengubah_nada >= 0:
                        kena_mutasi = ubah_random
                        kena_mutasi -= pilih_mengubah_nada
                        stop_mutasi += 1
                    komposisi[kena_mutasi_i][kena_mutasi_j] = kena_mutasi
            else:
                if pilih_operasi == "+" and kena_mutasi[k] + pilih_mengubah_nada <= range_nada:
                    if kena_mutasi[k] + pilih_mengubah_nada == 15 and k == 0:
                        continue
                    else:    
                        kena_mutasi[k] += pilih_mengubah_nada
                        stop_mutasi += 1
                elif kena_mutasi[k]-pilih_mengubah_nada >= 0:
                    kena_mutasi[k] -= pilih_mengubah_nada
                    stop_mutasi += 1
                komposisi[kena_mutasi_i][kena_mutasi_j][k] = kena_mutasi[k]

        else:
            if pilih_operasi == "+" and kena_mutasi + pilih_mengubah_nada <= range_nada+2:
                if kena_mutasi + pilih_mengubah_nada == 15 and kena_mutasi_j == 0:
                    continue
                else:
                    kena_mutasi += pilih_mengubah_nada
                    stop_mutasi += 1
            elif kena_mutasi-pilih_mengubah_nada >= 0:
                kena_mutasi -= pilih_mengubah_nada
                stop_mutasi += 1
            komposisi[kena_mutasi_i][kena_mutasi_j] = kena_mutasi
    
    # print(kena_mutasi_i,kena_mutasi_j)
    komposisi = change_durasi(komposisi, banyak_birama, anggota_birama, range_nada)

    stop_mutasi = 0
    while stop_mutasi < int(anggota_birama*probabilitas_mutasi*banyak_birama):
        kena_mutasi_i = random.randint(0,banyak_birama-1)
        kena_mutasi_j = random.randint(0,anggota_birama-1)
        kena_mutasi_i_sec = random.randint(0,banyak_birama-1)
        kena_mutasi_j_sec = random.randint(0,anggota_birama-1)
        if isinstance(komposisi[kena_mutasi_i][kena_mutasi_j], list) and isinstance(komposisi[kena_mutasi_i_sec][kena_mutasi_j_sec], list):
            k = random.randint(0,len(komposisi[kena_mutasi_i][kena_mutasi_j])-1)
            k_sec = random.randint(0,len(komposisi[kena_mutasi_i_sec][kena_mutasi_j_sec])-1)
            if komposisi[kena_mutasi_i][kena_mutasi_j][k] != range_nada and komposisi[kena_mutasi_i_sec][kena_mutasi_j_sec][k_sec] != range_nada:
                komposisi[kena_mutasi_i][kena_mutasi_j][k], komposisi[kena_mutasi_i_sec][kena_mutasi_j_sec][k_sec] = komposisi[kena_mutasi_i_sec][kena_mutasi_j_sec][k_sec], komposisi[kena_mutasi_i][kena_mutasi_j][k]
                stop_mutasi += 1
        elif isinstance(komposisi[kena_mutasi_i][kena_mutasi_j], list):
            k = random.randint(0,len(komposisi[kena_mutasi_i][kena_mutasi_j])-1)
            if komposisi[kena_mutasi_i][kena_mutasi_j][k] != range_nada and komposisi[kena_mutasi_i_sec][kena_mutasi_j_sec] != range_nada:
                komposisi[kena_mutasi_i][kena_mutasi_j][k], komposisi[kena_mutasi_i_sec][kena_mutasi_j_sec] = komposisi[kena_mutasi_i_sec][kena_mutasi_j_sec], komposisi[kena_mutasi_i][kena_mutasi_j][k]
                stop_mutasi += 1
        elif isinstance(komposisi[kena_mutasi_i_sec][kena_mutasi_j_sec], list):
            k_sec = random.randint(0,len(komposisi[kena_mutasi_i_sec][kena_mutasi_j_sec])-1)
            if komposisi[kena_mutasi_i][kena_mutasi_j] != range_nada and komposisi[kena_mutasi_i_sec][kena_mutasi_j_sec][k_sec] != range_nada:
                komposisi[kena_mutasi_i][kena_mutasi_j], komposisi[kena_mutasi_i_sec][kena_mutasi_j_sec][k_sec] = komposisi[kena_mutasi_i_sec][kena_mutasi_j_sec][k_sec], komposisi[kena_mutasi_i][kena_mutasi_j]
                stop_mutasi += 1
        else: 
            if komposisi[kena_mutasi_i][kena_mutasi_j] != range_nada and komposisi[kena_mutasi_i_sec][kena_mutasi_j_sec] != range_nada:
                komposisi[kena_mutasi_i][kena_mutasi_j], komposisi[kena_mutasi_i_sec][kena_mutasi_j_sec] = komposisi[kena_mutasi_i_sec][kena_mutasi_j_sec], komposisi[kena_mutasi_i][kena_mutasi_j]
                stop_mutasi += 1
    # print(kena_mutasi_i,kena_mutasi_j)

    # print("")
    # print(komposisi)
    # print("")

    return komposisi

# arr = [[13, 10, 6, 7], [[8, 0, 7, 5], [13, 3, 9, 0], [3, 2], [9, 5, 10, 0]], [[10, 0, 8, 12], 9, 12, 14], [11, 2, 13, 13], [7, [9, 10, 4, 2], 3, [1,2]]]
# arr2 = [[10, [2, 10, 3, 6], 6, 13], [8, 6, 7, [13, 1]], [10, [0, 12], 7, 15], [2, 15, 15, [8, 0, 5, 3]], [4, 0, [8, 5, 10, 11], 5]]
# arr3 = [[[4, 9, 5, 10], 6, 14, 2], [9, 6, 3, 11], [12, 11, 10, 7], [4, 12, 11, 14], [9, [9, 1, 6, 4], 7, 4], [8, 10, 11, 6], [6, 15, 1, 5], [4, [0, 5], 4, [3, 6]], [5, 15, 1, 6], [2, 14, 7, 0]]
# arr = [[[3, 9, 2, 10], [0, 12, 4, 6], [5, 15, 13, 12], [7, 1, [0, 10], 1], [5, [6, 11, 7, 4], 11, 3]], [[10, 4, 13, 9], [2, 1, 8, 3], [7, [0, 3, 12, 10], 1, 9], [5, 12, 4, 9], [8, 8, 8, 0]], [[5, 13, 7, 1], [13, 4, [4, 5, 7, 6], 2], [10, 5, 14, 0], [4, 5, 4, 2], [10, 13, [9, 4, 13, 2], 1]], [[8, 11, 2, [6, 2]], [11, 0, 6, 14], [[4, 7, 12, 1], 0, 1, 9], [7, 3, [3, 10], [13, 0]], [7, 8, [1, 12], 0]], [[9, 8, 4, 10], [[7, 8, 1, 11], 14, 11, 9], [[10, 9], 0, 4, 4], [7, 6, 9, 9], [0, 3, 2, 7]]]
# print(mutasi(arr[0], 5, 4, 50, 15))

# for i in range(100):
#     mutated = mutasi(arr2,5,4,100,15)

# print(mutated)

def mutasi_bass(komposisi, banyak_birama, anggota_birama, probabilitas_mutasi, range_nada):
    operasi = ["+","-"]
    mengubah_nada = [1,2,3,4,5,6]
    # for i in range(len(komposisi)):
    stop_mutasi = 0
    # print(int(anggota_birama*probabilitas_mutasi*banyak_birama))
    # while stop_mutasi < int(anggota_birama*probabilitas_mutasi*banyak_birama):
    #     kena_mutasi_i = random.randint(0,anggota_birama-1)
    #     if komposisi[kena_mutasi_i] != range_nada:
    #         pilih_operasi = random.choice(operasi)
    #         if pilih_operasi == "+" and komposisi[kena_mutasi_i] + 7 < range_nada:
    #             komposisi[kena_mutasi_i] += 7
    #             stop_mutasi += 1
    #         elif komposisi[kena_mutasi_i]-7 > 0:
    #             komposisi[kena_mutasi_i]-= 7
    #             stop_mutasi += 1

    # stop_mutasi = 0
    while stop_mutasi < int(anggota_birama*probabilitas_mutasi*banyak_birama):
        kena_mutasi_i = random.randint(0,anggota_birama-1)
        if komposisi[kena_mutasi_i] != range_nada:
            pilih_operasi = random.choice(operasi)
            pilih_mengubah_nada = random.choice(mengubah_nada)
            if pilih_operasi == "+" and komposisi[kena_mutasi_i] + pilih_mengubah_nada < range_nada:
                komposisi[kena_mutasi_i] += pilih_mengubah_nada
                stop_mutasi += 1
            elif komposisi[kena_mutasi_i]-pilih_mengubah_nada > 0:
                komposisi[kena_mutasi_i] -= pilih_mengubah_nada
                stop_mutasi += 1

    stop_mutasi = 0
    while stop_mutasi < int(anggota_birama*probabilitas_mutasi*banyak_birama):
        kena_mutasi_i = random.randint(0,anggota_birama-1)
        kena_mutasi_i_sec = random.randint(0,anggota_birama-1)
        if komposisi[kena_mutasi_i] != range_nada and komposisi[kena_mutasi_i_sec] != range_nada:
            komposisi[kena_mutasi_i], komposisi[kena_mutasi_i_sec] = komposisi[kena_mutasi_i_sec], komposisi[kena_mutasi_i]
            stop_mutasi += 1


    return komposisi