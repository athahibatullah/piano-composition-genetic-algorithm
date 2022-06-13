import numpy as np
import GA
import parameter_fitness as pf
import parameter_fitness_bass as pfb
import fungsi_fitness as ff
import csv
import tone_map as tm
import chord_map as cm

banyak_birama = int(input("Banyak birama: "))
banyak_individu = int(input("Banyak individu: "))
probabilitas_mutasi = int(input("Probabilitas mutasi: "))/100
banyak_generasi = 2
range_nada = 14+1
anggota_birama = 4
tangga_nada = 'C'
komposisi_treble = []
komposisi_bass = []

def generate_populasi(banyak_birama, anggota_birama, range_nada, komposisi_treble, komposisi_bass, banyak_individu):
    komposisi_treble_list = []
    komposisi_bass_list = []
    for i in range(banyak_individu):
        populasi_awal_treble = GA.inisialisasi_individu(banyak_birama, anggota_birama, range_nada, komposisi_treble)
        populasi_awal_bass = GA.inisialisasi_bass(1, anggota_birama+1, range_nada, komposisi_bass)
        komposisi_treble_list.append(populasi_awal_treble)
        komposisi_bass_list.append(populasi_awal_bass)
        komposisi_treble = []
        komposisi_bass = []
    return komposisi_treble_list, komposisi_bass_list

def hitung_fitness(populasi_awal, range_nada, banyak_birama, anggota_birama):
    total_fitness_list = []
    for i in range(len(populasi_awal)):
        variasi_nada_list = pf.variasi_nada(populasi_awal[i], range_nada, banyak_birama, anggota_birama)
        interval_disonan_list = pf.interval_disonan(populasi_awal[i],banyak_birama, anggota_birama,range_nada)
        arah_kontur_list = pf.arah_kontur(populasi_awal[i],banyak_birama,anggota_birama,range_nada)
        stabilitas_kontur_list = pf.stabilitas_kontur(populasi_awal[i], banyak_birama, anggota_birama, range_nada)
        variasi_irama_list = pf.variasi_irama(populasi_awal[i],banyak_birama,anggota_birama,range_nada)
        rentang_irama_list = pf.rentang_irama(populasi_awal[i],banyak_birama,anggota_birama,range_nada)
        
        fitness_birama_all = []
        for j in range(banyak_birama):
            fitness_birama = [variasi_nada_list[j],interval_disonan_list[j],arah_kontur_list[j],stabilitas_kontur_list[j],variasi_irama_list[j],rentang_irama_list[j]]
            fitness_birama_all.append(fitness_birama)
        sum_fitness_birama = ff.sum_fitness_birama(fitness_birama_all, banyak_birama)
        sum_fitness_birama_all = ff.sum_fitness_birama_all(sum_fitness_birama)
        interval_sum_list = ff.interval_sum(populasi_awal[i], banyak_birama, anggota_birama, range_nada)
        mean_interval_birama = ff.mean_interval_birama(interval_sum_list, anggota_birama)
        varian_interval_birama = ff.varian_interval_birama(interval_sum_list, mean_interval_birama, anggota_birama)
        sum_mean_interval_birama = ff.sum_mean_interval_birama(mean_interval_birama)
        sum_varian_interval_birama = ff.sum_varian_interval_birama(varian_interval_birama)
        total_fitness = ff.total_fitness(sum_mean_interval_birama,sum_varian_interval_birama,sum_fitness_birama_all)
        total_fitness_list.append(total_fitness)
    
    return total_fitness_list

def hitung_fitness_bass(populasi_awal, range_nada, anggota_birama):
    total_fitness_list = []
    for i in range(len(populasi_awal)):
        variasi_nada_list = pfb.variasi_nada(populasi_awal[i], range_nada)
        interval_disonan_list = pfb.interval_disonan(populasi_awal[i],1,anggota_birama,range_nada)
        arah_kontur_list = pfb.arah_kontur(populasi_awal[i],anggota_birama)
        stabilitas_kontur_list = pfb.stabilitas_kontur(populasi_awal[i], anggota_birama, range_nada)
        variasi_irama_list = pfb.variasi_irama(populasi_awal[i],banyak_birama,anggota_birama,range_nada)
        rentang_irama_list = pfb.rentang_irama(populasi_awal[i],banyak_birama,anggota_birama,range_nada)
        
        fitness_birama = [variasi_nada_list,interval_disonan_list,arah_kontur_list,stabilitas_kontur_list,variasi_irama_list,rentang_irama_list]
        sum_fitness_birama = ff.sum_fitness_birama_all(fitness_birama)
        interval_sum_list = ff.interval_sum_bass(populasi_awal[i], anggota_birama)
        mean_interval_birama = ff.mean_interval_birama(interval_sum_list, anggota_birama)
        varian_interval_birama = ff.varian_interval_birama(interval_sum_list, mean_interval_birama, anggota_birama)
        sum_mean_interval_birama = ff.sum_mean_interval_birama(mean_interval_birama)
        sum_varian_interval_birama = ff.sum_varian_interval_birama(varian_interval_birama)
        total_fitness = ff.total_fitness(sum_mean_interval_birama,sum_varian_interval_birama,sum_fitness_birama)
        total_fitness_list.append(total_fitness)
    
    return total_fitness_list


def update_generasi(populasi_next, total_fitness_list, banyak_individu):
    fitness_dict = {}
    for i, val in enumerate(total_fitness_list):
        fitness_dict[val] = i
    next_gen_list = []
    hasil_seleksi = GA.seleksi_turnamen(total_fitness_list, 3, banyak_individu)
    
    for val in hasil_seleksi:
        next_gen_list.append(populasi_next[fitness_dict[val]])
    return next_gen_list

def mutasi_generasi(populasi_treble, populasi_bass, banyak_birama, anggota_birama, probabilitas_mutasi, range_nada, banyak_individu):
    treble_mutasi_list = []
    bass_mutasi_list = []
    for i in range(banyak_individu):
        treble_mutasi_list.append(GA.mutasi(populasi_treble[i], banyak_birama, anggota_birama, probabilitas_mutasi, range_nada))
        bass_mutasi_list.append(GA.mutasi_bass(populasi_bass[i], 1, anggota_birama+1, probabilitas_mutasi, range_nada))
    return treble_mutasi_list, bass_mutasi_list

if __name__ == "__main__":
    populasi_awal = generate_populasi(banyak_birama, anggota_birama, range_nada, komposisi_treble, komposisi_bass, banyak_individu)
    populasi_awal_treble = populasi_awal[0]
    populasi_awal_bass = populasi_awal[1]
    total_fitness_treble_list = hitung_fitness(populasi_awal_treble, range_nada, banyak_birama, anggota_birama)
    total_fitness_bass_list = hitung_fitness_bass(populasi_awal_bass, range_nada, anggota_birama+1)
    # print("Total fitness: " , max(total_fitness_list))
    # with open('composition.csv', 'w', newline='') as file:
    #     writer = csv.writer(file)
    #     for i in range(len(populasi_awal)):
    #         writer.writerow(populasi_awal[i])
    
    max_fitness_indiv = 0
    max_fitness = 0
    populasi_next_treble = populasi_awal[0]
    populasi_next_bass = populasi_awal[1]
    best_fitness_list = []
    for i in range(banyak_generasi-1):
        populasi_next_treble = update_generasi(populasi_next_treble, total_fitness_treble_list, banyak_individu)
        populasi_next_bass = update_generasi(populasi_next_bass, total_fitness_bass_list, banyak_individu)
        hasil_mutasi = mutasi_generasi(populasi_next_treble, populasi_next_bass, banyak_birama, anggota_birama, probabilitas_mutasi, range_nada, banyak_individu)
        hasil_mutasi_treble = hasil_mutasi[0]
        hasil_mutasi_bass = hasil_mutasi[1]
        populasi_next_treble = hasil_mutasi_treble
        populasi_next_bass = hasil_mutasi_bass

        # print(populasi_next)
        
        total_fitness_list = hitung_fitness(populasi_next_treble, range_nada, banyak_birama, anggota_birama)
        best_fitness_list.append(max(total_fitness_list))
        if max_fitness < max(total_fitness_treble_list):
            max_fitness = max(total_fitness_treble_list)
            max_fitness_indiv = populasi_next_treble[total_fitness_treble_list.index(max_fitness)]

    # # print(best_fitness_list)
    # # print(max_fitness)
    # # print(max_fitness_indiv)
    # print(populasi_next_treble)
    # print(populasi_next_bass)

    translated = []
    # translated_best = tm.translate(max_fitness_indiv, banyak_birama, anggota_birama, range_nada, tangga_nada)
    translated_chord = []
    # translated_chord_best = cm.translate(max_fitness_indiv, anggota_birama, range_nada, tangga_nada)
    for i in range(len(populasi_next_treble)):
        translated.append(tm.translate(populasi_next_treble[i], banyak_birama, anggota_birama, range_nada, tangga_nada))
    temp_translated= []
    for i in range(len(populasi_next_bass)):
        temp_individu = []
        for j in range(anggota_birama+1):
            temp_birama = []
            for k in range(anggota_birama):
                temp_birama.append(populasi_next_bass[i][j])
            temp_individu.append(temp_birama)
        temp_translated.append(temp_individu)
    for i in range(len(temp_translated)):
        translated_chord.append(cm.translate(temp_translated[i], anggota_birama, range_nada, tangga_nada))
    # print(translated_chord)
    def scale(tangga_nada):
        return {
            'C': 'c',
            'D': 'd',
            'E': 'e',
            'F': 'f',
            'G': 'g',
            'A': 'a',
            'B': 'b',
            'Db': 'des',
            'Eb': 'es',
            'Fs': 'fis',
            'Ab': 'as',
            'Bb': 'bes'
        }[tangga_nada]
    tangga_nada = scale(tangga_nada)

    title = """\header {
                title = "Composition Generated by Genetic Algorithm"
                composer = "Mr. GA"
            }\n"""
    for i in range(1, banyak_individu+1):

        # content = "\\fixed c' {\n" + "\key " + tangga_nada + " \major" + "\n" +str(translated[i-1]) + '\n' "}"
        content = "<<\n \\new Staff \\fixed c' {\n" + "\key " + tangga_nada + " \major" + "\n" +str(translated[i-1]) + '\n' "}\n" + "\\new Staff \\fixed c, {\n" + "\key " + tangga_nada + " \major " + "\clef bass" + " \\chordmode{ \n" + str(translated_chord[i-1]) + "}" +  '\n' "}\n" +">>"
        # print(content)
        f = open('output/test ' + str(i) + '.ly', 'w')
        # f = open('output/test ' + str(i) + '.txt', 'w')
        f.write(title + content)
        f.close()

        content_midi = "\\score {\n" + content + "\n" + "\\midi{ }\n}"
        # print(content_midi)
        f = open('output/test_midi ' + str(i) + '.ly', 'w')
        f.write(title + content_midi)
        f.close()

    # content = "\\fixed c' {\n" + "\key " + tangga_nada + " \major" + "\n" +str(translated_best) + '\n' "}"
    # # print(content)
    # f = open('output/best.ly', 'w')
    # f.write(title + content)
    # f.close()

    # content_midi = "\\score {\n" + content + "\n" + "\\midi{ }\n}"
    # # print(content_midi)
    # f = open('output/best_midi.ly', 'w')
    # f.write(title + content_midi)
    # f.close()

    # # with open('composition_translated.csv', 'w', newline='') as file:
    # #     writer = csv.writer(file)
    # #     for i in range(len(translated)):
    # #         writer.writerow(translated[i])