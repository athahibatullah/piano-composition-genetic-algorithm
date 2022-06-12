from numpy import nanmax


def variasi_nada(komposisi, range_nada, banyak_birama, anggota_birama):
    variasi_nada_list = []
    for i in range(banyak_birama):
        banyak_nada_digunakan = 0
        for j in range(1, range_nada):        
            if j in komposisi[i]:
                banyak_nada_digunakan += 1
        for j in range(anggota_birama):
             if isinstance(komposisi[i][j], list):
                 for k in range(1, range_nada):        
                    if k in komposisi[i][j] and k not in komposisi[i]:
                        banyak_nada_digunakan += 1
        variasi_nada_list.append(banyak_nada_digunakan/(range_nada-1))

    return variasi_nada_list


def hitung_interval(komposisi, banyak_birama, anggota_birama, parameter):
    komposisi_merge = []
    for i in range(banyak_birama):
        birama_merge = []
        for j in range(anggota_birama):
            if isinstance(komposisi[i][j], list):
                for k in range(len(komposisi[i][j])):
                    birama_merge.append(komposisi[i][j][k])
            else:
                birama_merge.append(komposisi[i][j])
        komposisi_merge.append(birama_merge)
    interval_list = []
    for i in range(len(komposisi_merge)):
        interval_list_birama = []
        for j in range(len(komposisi_merge[i])-1):
            if parameter == "interval_disonan":
                interval = abs(komposisi_merge[i][j]-komposisi_merge[i][j+1])
            else:
                interval = komposisi_merge[i][j]-komposisi_merge[i][j+1]
            interval_list_birama.append(interval)
        interval_list.append(interval_list_birama)

    return interval_list

def komposisi_convert(komposisi, banyak_birama, anggota_birama, range_nada):
    for i in range(banyak_birama):
        for j in range(anggota_birama-1):
            if j != anggota_birama and komposisi[i][j+1] == range_nada and not isinstance(komposisi[i][j+1],list):
                komposisi[i][j+1] = komposisi[i][j]

    return komposisi

def interval_disonan(komposisi, banyak_birama, anggota_birama, range_nada):
    interval_list = {0: [0,1,2,3,4,5,7,8,9,12], 0.5: 10, 1: [6,11,13]}
    interval_disonan_list = []
    konversi_komposisi = komposisi_convert(komposisi, banyak_birama, anggota_birama, range_nada)
    interval = hitung_interval(konversi_komposisi,banyak_birama,anggota_birama,"interval_disonan")
    print(interval)
    for i in range(len(interval)):
        sum_interval_disonan = 0
        for j in range(len(interval[i])):
            if interval[i][j] in interval_list[1]:
                sum_interval_disonan += 1
            elif interval[i][j] == interval_list[0.5]:
                sum_interval_disonan += 0.5
        interval_disonan_list.append(sum_interval_disonan/(range_nada-2))

    return interval_disonan_list

def arah_kontur(komposisi, banyak_birama, anggota_birama, range_nada):
    arah_kontur_naik_list = []
    interval_sum = 0
    konversi_komposisi = komposisi_convert(komposisi, banyak_birama, anggota_birama, range_nada)
    interval = hitung_interval(konversi_komposisi,banyak_birama,anggota_birama,"arah_kontur")
    print(interval)
    for i in range(len(interval)):
        arah_kontur_sum = 0
        for j in range(len(interval[i])):
            interval_sum += abs(interval[i][j])
            if interval[i][j] < 0:
                arah_kontur_sum += abs(interval[i][j])
        print(interval_sum)
        arah_kontur_naik_list.append(arah_kontur_sum)
    return [x/interval_sum for x in arah_kontur_naik_list]

def stabilitas_kontur(komposisi, banyak_birama, anggota_birama, range_nada):
    stabilitas_kontur_list = []
    konversi_komposisi = komposisi_convert(komposisi, banyak_birama, anggota_birama, range_nada)
    interval = hitung_interval(konversi_komposisi,banyak_birama,anggota_birama,"stabilitas_kontur")

    for i in range(banyak_birama):
        stabilitas_kontur_count = 0
        for j in range(len(interval)-1):
            if interval[i][j] == 0 and interval[i][j+1] == 0:
                stabilitas_kontur_count += 1
        stabilitas_kontur_list.append(stabilitas_kontur_count/(len(interval)-1))
    return stabilitas_kontur_list

def hitung_durasi(komposisi, anggota_birama, range_nada):
    min_durasi = 1
    max_durasi = 1
    durasi_list = [1]
    for i in range(anggota_birama):
        if isinstance(komposisi[i],list):
            if len(komposisi[i]) == 2 and min_durasi > 0.25:
                min_durasi = 0.5
            elif len(komposisi[i]) == 4:
                min_durasi = 0.25

            if min_durasi not in durasi_list:
                durasi_list.append(min_durasi)
        elif komposisi[i] == range_nada:
            if i != anggota_birama-1 and komposisi[i] == range_nada:
                max_durasi = 4
            elif max_durasi < 4:
                max_durasi = 2
            if max_durasi not in durasi_list:
                durasi_list.append(max_durasi)
    return min_durasi, max_durasi, durasi_list

def variasi_irama(komposisi, banyak_birama, anggota_birama, range_nada):
    variasi_irama_list = []
    for i in range(banyak_birama):
        banyak_durasi_beda = len(hitung_durasi(komposisi[i], anggota_birama, range_nada)[2])
        variasi_irama_list.append(banyak_durasi_beda/16)
    return variasi_irama_list

def rentang_irama(komposisi, banyak_birama, anggota_birama, range_nada):
    rentang_irama_list = []
    for i in range(banyak_birama):
        durasi = hitung_durasi(komposisi[i], anggota_birama, range_nada)
        min_durasi = durasi[0]
        max_durasi = durasi[1]
        print(min_durasi,max_durasi)
        rentang_irama_list.append((max_durasi/min_durasi)/16)
    return rentang_irama_list

# arr = [[13, 10, 6, 7], [[8, 0, 7, 5], [13, 3, 9, 0], [3, 2], [9, 5, 10, 0]], [[10, 0, 8, 12], 9, 12, 14], [11, 2, 13, 13], [7, [9, 10, 4, 2], 3, [1,2]]]
# arr2 = [[10, [2, 10, 3, 6], 6, 13], [8, 6, 7, [13, 1]], [10, [0, 12], 7, 15], [2, 15, 15, [8, 0, 5, 3]], [4, 0, [8, 5, 10, 11], 5]]
# # print(stabilitas_kontur(arr2,5,4,15))
# # print(interval_disonan(arr2,5,4,15))
# # print(arah_kontur(arr2, 5, 4, 15))
# print(rentang_irama(arr2,5,4,15))