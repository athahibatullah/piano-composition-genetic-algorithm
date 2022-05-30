import numpy as np
import random
import GA
import parameter_fitness as pf
import fungsi_fitness as ff
import csv
import tone_map as tm
import chord_map as cm

banyak_birama = int(input("Banyak birama: "))
banyak_individu = int(input("Banyak individu: "))
probabilitas_mutasi = int(input("Probabilitas mutasi: "))/100
banyak_generasi = 2
range_nada = 14+1
anggota_birama = 10
tangga_nada = 'E'
komposisi = np.empty((banyak_birama,anggota_birama))

def generate_populasi(banyak_birama, anggota_birama, range_nada, komposisi, banyak_individu):
    komposisi_individu_list = []
    for i in range(banyak_individu):
        populasi_awal = GA.inisialisasi_individu(banyak_birama, anggota_birama, range_nada, komposisi)
        populasi_awal = populasi_awal
        komposisi_individu_list.append(populasi_awal)
        komposisi = np.empty((banyak_birama,anggota_birama))
    return komposisi_individu_list

def hitung_fitness(populasi_awal, range_nada, banyak_birama, anggota_birama):
    total_fitness_list = []
    for i in range(len(populasi_awal)):
        variasi_nada_list = pf.variasi_nada(populasi_awal[i], range_nada, banyak_birama)
        interval_disonan_list = pf.interval_disonan(populasi_awal[i],anggota_birama,range_nada)
        arah_kontur_list = pf.arah_kontur(populasi_awal[i],anggota_birama)
        stabilitas_kontur_list = pf.stabilitas_kontur(populasi_awal[i], anggota_birama)
        variasi_irama_list = pf.variasi_irama(populasi_awal[i],anggota_birama,range_nada)
        rentang_irama_list = pf.rentang_irama(populasi_awal[i],anggota_birama,range_nada)
        
        fitness_birama_all = []
        for j in range(banyak_birama):
            fitness_birama = [variasi_nada_list[j],interval_disonan_list[j],arah_kontur_list[j],stabilitas_kontur_list[j],variasi_irama_list[j],rentang_irama_list[j]]
            fitness_birama_all.append(fitness_birama)
        sum_fitness_birama = ff.sum_fitness_birama(fitness_birama_all, banyak_birama)
        sum_fitness_birama_all = ff.sum_fitness_birama_all(sum_fitness_birama)
        interval_sum_list = ff.interval_sum(populasi_awal[i], anggota_birama)
        mean_interval_birama = ff.mean_interval_birama(interval_sum_list, anggota_birama)
        varian_interval_birama = ff.varian_interval_birama(interval_sum_list, mean_interval_birama, anggota_birama)
        sum_mean_interval_birama = ff.sum_mean_interval_birama(mean_interval_birama)
        sum_varian_interval_birama = ff.sum_varian_interval_birama(varian_interval_birama)
        total_fitness = ff.total_fitness(sum_mean_interval_birama,sum_varian_interval_birama,sum_fitness_birama_all)
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

def mutasi_generasi(populasi_awal, banyak_birama, anggota_birama, probabilitas_mutasi, range_nada, banyak_individu):
    individu_mutasi_list = []
    for i in range(banyak_individu):
        individu_mutasi_list.append(GA.mutasi(populasi_awal[i], banyak_birama, anggota_birama, probabilitas_mutasi, range_nada))

    return individu_mutasi_list

if __name__ == "__main__":
    populasi_awal = generate_populasi(banyak_birama, anggota_birama, range_nada, komposisi, banyak_individu)
    populasi_awal = populasi_awal
    # print(populasi_awal)
    total_fitness_list = hitung_fitness(populasi_awal, range_nada, banyak_birama, anggota_birama)
    # print("Total fitness: " , max(total_fitness_list))
    with open('composition.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(populasi_awal)):
            writer.writerow(populasi_awal[i])
    
    
    max_fitness_indiv = 0
    max_fitness = 0
    populasi_next = populasi_awal
    best_fitness_list = []
    for i in range(banyak_generasi-1):
        populasi_next = update_generasi(populasi_next, total_fitness_list, banyak_individu)
        hasil_mutasi = mutasi_generasi(populasi_awal, banyak_birama, anggota_birama, probabilitas_mutasi, range_nada, banyak_individu)
        populasi_next = hasil_mutasi

        # print(populasi_next)
        
        total_fitness_list = hitung_fitness(populasi_next, range_nada, banyak_birama, anggota_birama)
        best_fitness_list.append(max(total_fitness_list))
        if max_fitness < max(total_fitness_list):
            max_fitness = max(total_fitness_list)
            max_fitness_indiv = populasi_next[total_fitness_list.index(max_fitness)]

    print(best_fitness_list)
    print(max_fitness)
    print(max_fitness_indiv)

    translated = []
    translated_best = tm.translate(max_fitness_indiv, anggota_birama, range_nada, tangga_nada)
    translated_chord = []
    translated_chord_best = cm.translate(max_fitness_indiv, anggota_birama, range_nada, tangga_nada)
    for i in range(len(populasi_next)):
        translated.append(tm.translate(populasi_next[i], anggota_birama, range_nada, tangga_nada))
    for i in range(len(populasi_next)):
        translated_chord.append(cm.translate(populasi_next[i], anggota_birama, range_nada, tangga_nada))
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

    content = "\\fixed c' {\n" + "\key " + tangga_nada + " \major" + "\n" +str(translated_best) + '\n' "}"
    # print(content)
    f = open('output/best.ly', 'w')
    f.write(title + content)
    f.close()

    content_midi = "\\score {\n" + content + "\n" + "\\midi{ }\n}"
    # print(content_midi)
    f = open('output/best_midi.ly', 'w')
    f.write(title + content_midi)
    f.close()

    # with open('composition_translated.csv', 'w', newline='') as file:
    #     writer = csv.writer(file)
    #     for i in range(len(translated)):
    #         writer.writerow(translated[i])