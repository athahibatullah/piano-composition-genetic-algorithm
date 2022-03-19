def variasi_nada(komposisi, range_nada, banyak_birama):
    banyak_nada_list = []
    for i in range(banyak_birama):
        banyak_nada_digunakan = 1
        for j in range(1, range_nada):
            if j in komposisi[i]:
                banyak_nada_digunakan += 1
        banyak_nada_list.append(banyak_nada_digunakan/range_nada)

    return komposisi, banyak_nada_list

def interval_disonan(komposisi, anggota_birama, range_nada):
    interval_list = {0: [0,1,2,3,4,5,7,8,9,12], 0.5: 10, 1: [6,11,13]}
    interval_disonan_list = []
    for i in range(len(komposisi)):
        sum_interval_disonan = 0
        for j in range(anggota_birama-1):
            interval = abs(komposisi[i][j]-komposisi[i][j+1])
            if interval in interval_list[1]:
                sum_interval_disonan += 1
            elif interval == interval_list[0.5]:
                sum_interval_disonan += 0.5
        interval_disonan_list.append(sum_interval_disonan/range_nada)

    return interval_disonan_list

def arah_kontur(komposisi, anggota_birama):
    arah_kontur_naik_list = []
    interval_sum = 0
    for i in range(len(komposisi)):
        arah_kontur_sum = 0
        for j in range(anggota_birama-1):
            interval = komposisi[i][j]-komposisi[i][j+1]
            interval_sum += abs(interval)
            if interval < 0:
                arah_kontur_sum += abs(interval)
        arah_kontur_naik_list.append(arah_kontur_sum)
    return arah_kontur_naik_list/interval_sum

def stabilitas_kontur(komposisi, anggota_birama):
    stabilitas_kontur_list = []
    for i in range(len(komposisi)):
        interval_list = []
        stabilitas_kontur_count = 0
        for j in range(anggota_birama-1):
            interval = komposisi[i][j]-komposisi[i][j+1]
            interval_list.append(interval)
        for k in range(len(interval_list)-1):
            if interval_list[k] == 0 and interval_list[k+1] == 0:
                stabilitas_kontur_count += 1
        stabilitas_kontur_list.append(stabilitas_kontur_count/len(interval_list))
    return stabilitas_kontur_list
            
def variasi_irama(komposisi, anggota_birama, range_nada):
    variasi_irama_list = []
    for i in range(len(komposisi)):
        variasi_irama_rekor = 1
        for j in range(anggota_birama-1):
            variasi_irama_counter = 0
            if komposisi[i][j] == range_nada and j != anggota_birama-2:
                while komposisi[i][j] == range_nada:
                    variasi_irama_counter += 1
                    if variasi_irama_counter > variasi_irama_rekor:
                        variasi_irama_rekor += 1
                    j+=1

        variasi_irama_list.append(variasi_irama_rekor/16)
    return variasi_irama_list

def rentang_irama(komposisi, anggota_birama, range_nada, durasi_minimal=1):
    rentang_irama = variasi_irama(komposisi, anggota_birama, range_nada)
    rentang_irama = [x*16 for x in rentang_irama]
    rentang_irama_list = [(x/durasi_minimal)/16 for x in rentang_irama]
    return rentang_irama_list