def variasi_nada(komposisi, range_nada):
    banyak_nada_digunakan = 1
    for j in range(1, range_nada):
        if j in komposisi:
            banyak_nada_digunakan += 1

    return banyak_nada_digunakan/(range_nada-1)

def interval_disonan(komposisi, banyak_birama, anggota_birama, range_nada):
    interval_list = {0: [0,1,2,3,4,5,7,8,9,12], 0.5: 10, 1: [6,11,13]}
    sum_interval_disonan = 0
    for i in range(anggota_birama-1):
        interval = abs(komposisi[i]-komposisi[i+1])
        if interval in interval_list[1]:
            sum_interval_disonan += 1
        elif interval == interval_list[0.5]:
            sum_interval_disonan += 0.5

    return sum_interval_disonan/(range_nada-2)

def arah_kontur(komposisi, anggota_birama):
    interval_sum = 0
    arah_kontur_sum = 0
    for i in range(anggota_birama-1):
        interval = komposisi[i]-komposisi[i+1]
        interval_sum += abs(interval)
        if interval < 0:
            arah_kontur_sum += abs(interval)
    return arah_kontur_sum/interval_sum

def stabilitas_kontur(komposisi, anggota_birama, range_nada):
    for i in range(anggota_birama-1):
        if i != anggota_birama and komposisi[i+1] == range_nada:
            komposisi[i+1] = komposisi[i]

    interval_list = []
    stabilitas_kontur_count = 0
    for j in range(anggota_birama-1):
        interval = komposisi[j]-komposisi[j+1]
        interval_list.append(interval)
    for k in range(len(interval_list)-1):
        if interval_list[k] == 0 and interval_list[k+1] == 0:
            stabilitas_kontur_count += 1
    return stabilitas_kontur_count/(len(interval_list)-1)

def hitung_durasi(komposisi, anggota_birama, range_nada):
    min_durasi = 1
    max_durasi = 1
    durasi_list = [1]
    print(komposisi)
    for i in range(anggota_birama):
        if komposisi[i] == range_nada:
            if i != anggota_birama-1 and komposisi[i] == range_nada:
                max_durasi = 4
            elif max_durasi < 4:
                max_durasi = 2
            if max_durasi not in durasi_list:
                durasi_list.append(max_durasi)
    return min_durasi, max_durasi, durasi_list

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