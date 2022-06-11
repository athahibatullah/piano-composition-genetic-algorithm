def variasi_nada(komposisi, range_nada):
    banyak_nada_digunakan = 1
    for j in range(1, range_nada):
        if j in komposisi:
            banyak_nada_digunakan += 1

    return banyak_nada_digunakan/range_nada

def interval_disonan(komposisi, anggota_birama, range_nada):
    interval_list = {0: [0,1,2,3,4,5,7,8,9,12], 0.5: 10, 1: [6,11,13]}
    sum_interval_disonan = 0
    for i in range(anggota_birama-1):
        interval = abs(komposisi[i]-komposisi[i+1])
        if interval in interval_list[1]:
            sum_interval_disonan += 1
        elif interval == interval_list[0.5]:
            sum_interval_disonan += 0.5

    return sum_interval_disonan/range_nada

def arah_kontur(komposisi, anggota_birama):
    interval_sum = 0
    arah_kontur_sum = 0
    for i in range(anggota_birama-1):
        interval = komposisi[i]-komposisi[i+1]
        interval_sum += abs(interval)
        if interval < 0:
            arah_kontur_sum += abs(interval)
    return arah_kontur_sum/interval_sum

def stabilitas_kontur(komposisi, anggota_birama):
    range_nada = 15

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
def variasi_irama(komposisi, anggota_birama, range_nada):
    variasi_irama_rekor = 1
    for i in range(anggota_birama-1):
        variasi_irama_counter = 0
        if komposisi[i] == range_nada and i < anggota_birama-1:
            while komposisi[i] == range_nada and i < anggota_birama-1:
                variasi_irama_counter += 1
                if variasi_irama_counter > variasi_irama_rekor:
                    variasi_irama_rekor += 1
                i+=1
    return variasi_irama_rekor/16

def rentang_irama(komposisi, anggota_birama, range_nada, durasi_minimal=1):
    rentang_irama = variasi_irama(komposisi, anggota_birama, range_nada)
    rentang_irama = rentang_irama*16
    rentang_irama_list = (rentang_irama/durasi_minimal)/16 
    return rentang_irama_list