def variasi_nada(komposisi, range_nada):
    banyak_nada_digunakan = 0
    for j in range(1, range_nada+1):
        if j in komposisi:
            banyak_nada_digunakan += 1

    return banyak_nada_digunakan/(range_nada)

def hitung_interval_bass(komposisi, anggota_birama, parameter):
    interval_list = []
    for i in range(anggota_birama-1):
        if parameter == "interval_disonan" or parameter == "interval_sum":
            interval = abs(komposisi[i]-komposisi[i+1])
        else:
            interval = komposisi[i]-komposisi[i+1]
        interval_list.append(interval)
    return interval_list

# arr = [[6, 7, 5, 7, 3], [8, 2, 3, 6, 8], [6, 5, 5, 5, 6], [3, 7, 6, 5, 6], [1, 5, 4, 7, 1]]
# for i in range(len(arr)):
#     print(hitung_interval_bass(arr[i],5,"interval_disonan"))

def interval_disonan(komposisi, anggota_birama, range_nada):
    interval_list = {0: [0,1,2,3,4,5,7,8,9,12], 0.5: 10, 1: [6,11,13]}
    sum_interval_disonan = 0
    interval = hitung_interval_bass(komposisi, anggota_birama, "interval_disonan")
    for i in range(len(interval)):
        if interval[i] in interval_list[1]:
            sum_interval_disonan += 1
        elif interval[i] == interval_list[0.5]:
            sum_interval_disonan += 0.5

    return sum_interval_disonan/(range_nada-1)

def arah_kontur(komposisi, anggota_birama):
    interval_sum = 0
    interval = hitung_interval_bass(komposisi, anggota_birama, "arah_kontur")
    arah_kontur_sum = 0
    for i in range(len(interval)):
        interval_sum += abs(interval[i])
        if interval[i] < 0: #Jika minus berarti interval naik
            arah_kontur_sum += abs(interval[i])
    if interval_sum == 0:
        return arah_kontur_sum/(interval_sum+1)
    else:
        return arah_kontur_sum/(interval_sum)

def stabilitas_kontur(komposisi, anggota_birama, range_nada):
    interval = hitung_interval_bass(komposisi, anggota_birama, "stabilitas_kontur")
    stabilitas_kontur_count = 0
    for i in range(len(interval)-1):
        if interval[i] == 0 and interval[i+1] == 0:
            stabilitas_kontur_count += 1
    return stabilitas_kontur_count/(len(interval)-1)

def hitung_durasi(komposisi, anggota_birama, range_nada):
    min_durasi = 1
    max_durasi = 1
    durasi_list = [1]
    for i in range(anggota_birama):
        if komposisi[i] == range_nada:
            if i != anggota_birama-1 and komposisi[i] == range_nada:
                max_durasi = 4
            elif max_durasi < 4:
                max_durasi = 2
            if max_durasi not in durasi_list:
                durasi_list.append(max_durasi)
    return min_durasi, max_durasi, durasi_list
# arr = [[7, 6, 5, 2, 4], [3, 6, 5, 6, 3], [4, 8, 8, 4, 5], [5, 2, 6, 1, 3], [4, 6, 8, 4, 2]]
# arr = [[8, 1, 8, 7, 1], [8, 7, 2, 4, 8], [1, 4, 8, 2, 4], [6, 6, 6, 1, 5], [7, 8, 3, 8, 1]]
# arr = [[3, 8, 7, 5, 7], [6, 1, 3, 3, 6], [6, 5, 3, 7, 3], [7, 3, 8, 4, 4], [5, 6, 3, 6, 7]]
# arr = [[1, 8, 5, 6, 5], [2, 5, 3, 3, 8], [3, 4, 4, 1, 7], [7, 8, 5, 7, 7], [2, 7, 3, 7, 3]]
# for i in range(len(arr)):
# #     print(interval_disonan(arr[i],4,8))
#     # print(variasi_nada(arr[i], 8))
#     # print(hitung_interval_bass(arr[i], 4, "interval_disonan" ))
#     # print(arah_kontur(arr[i],5))
#     print(stabilitas_kontur(arr[i],5,8))


def variasi_irama(komposisi, banyak_birama, anggota_birama, range_nada):
    # variasi_irama_list = []
    # for i in range(banyak_birama):
    #     banyak_durasi_beda = len(hitung_durasi(komposisi[i], anggota_birama, range_nada)[2])
    #     variasi_irama_list.append(banyak_durasi_beda/16)
    # variasi_irama_list.append(0/16)
    return 0/16

def rentang_irama(komposisi, banyak_birama, anggota_birama, range_nada):
    min_durasi = 1
    max_durasi = 1
    # for i in range(banyak_birama):
    #     durasi = pf.hitung_durasi(komposisi[i], anggota_birama, range_nada)
    #     min_durasi = durasi[0]
    #     max_durasi = durasi[1]
        # rentang_irama_list.append((max_durasi/min_durasi)/16)
    # rentang_irama_list.append((max_durasi/min_durasi)/16)
    return (max_durasi/min_durasi)/16

def chord_progression(komposisi, fitness_bonus):
    # progression_1 = [[1,4,5],[4,5,1],[5,1,4]]
    progression_1 = [1,4,5]
    progression_2 = [4,5,1]
    progression_3 = [5,1,4]
    bonus_counter_list = []
    for i in range(len(komposisi)):
        bonus_counter = 0
        in_counting = False
        for j in range(len(komposisi[i])):
            if komposisi[i][j] in progression_2 and j != len(komposisi[i])-1:
                for k in range(len(progression_2)):
                    # print(i,j,komposisi[i][j])
                    if komposisi[i][j] == progression_2[k]:
                        # print(komposisi[i][j], progression_1[k][l])
                        print(i,j,komposisi[i][j], progression_2[k])
                        if not in_counting:
                            in_counting = True
                        bonus_counter += 1
                        break
                    elif in_counting and komposisi[i][j] != progression_2[k]:
                        print(i,j,komposisi[i][j], progression_2[k])
                        in_counting = False
                        bonus_counter = 0
                        break
            if in_counting:
                continue
        bonus_counter_list.append(bonus_counter)
    # for i in range(len(komposisi)):
    #     bonus_counter = 0
    #     in_counting = False
    #     for j in range(len(komposisi[i])):
    #         for k in range(len(progression_1)):
    #             if komposisi[i][j] in progression_1[k] and j != len(komposisi[i])-1:
    #                 for l in range(len(progression_1[k])):
    #                     # print()
    #                     if komposisi[i][j] == progression_1[k][l]:
    #                         # print(komposisi[i][j], progression_1[k][l])
    #                         if not in_counting:
    #                             in_counting = True
    #                         bonus_counter += 1
    #                         break
    #                     elif in_counting and komposisi[i][j] != progression_1[k][l]:
    #                         print(i,j,komposisi[i][j], progression_1[k][l])
    #                         in_counting = False
    #                         bonus_counter = 0
    #                         break
    #                 # if in_counting:
    #                 #     break
    #             if in_counting:
    #                 break
    #     bonus_counter_list.append(bonus_counter)
    return bonus_counter_list

# arr = [[9, 7, 11, 2, 2], [7, 3, 3, 8, 13], [4, 9, 2, 13, 3], [3, 7, 8, 6, 7], [7, 2, 6, 2, 3]]
# # arr = [[4,5,1,3,2],[1,4,9,2,1]]
# arr = [[4,5,1,3,2]]

# print(chord_progression(arr,50))

# [4,5,1]
# [4,5,1]
