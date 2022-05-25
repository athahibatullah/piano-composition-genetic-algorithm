C = {
        0: "r", 1: "c", 2: "d", 3: "e", 4: "f", 5: "g", 
        6: "a", 7: "b", 8: "cu", 9: "du", 10: "eu", 
        11: "fu", 12: "gu", 13: "au", 14: "bu", 15: "p" 
    }
D = {
        0: "r", 1: "d", 2: "e", 3: "fis", 4: "g", 5: "a", 
        6: "b", 7: "cis", 8: "du", 9: "eu", 10: "fisu", 
        11: "gu", 12: "au", 13: "bu", 14: "cisu", 15: "p" 
    }
E = {
        0: "r", 1: "e", 2: "fis", 3: "gis", 4: "a", 5: "b", 
        6: "cis", 7: "dis", 8: "eu", 9: "fisu", 10: "gisu", 
        11: "au", 12: "bu", 13: "cisu", 14: "disu", 15: "p" 
    }
F = {
        0: "r", 1: "f", 2: "g", 3: "a", 4: "bes", 5: "c", 
        6: "d", 7: "e", 8: "fu", 9: "gu", 10: "au", 
        11: "besu", 12: "cu", 13: "du", 14: "eu", 15: "p" 
    }
G = {
        0: "r", 1: "g", 2: "a", 3: "b", 4: "c", 5: "d", 
        6: "e", 7: "fis", 8: "gu", 9: "au", 10: "bu", 
        11: "cu", 12: "du", 13: "eu", 14: "fisu", 15: "p" 
    }
A = {
        0: "r", 1: "al", 2: "bl", 3: "cis", 4: "d", 5: "e", 
        6: "fis", 7: "gis", 8: "au", 9: "bu", 10: "cisu", 
        11: "du", 12: "eu", 13: "fisu", 14: "gisu", 15: "p" 
    }
B = {
    0: "r", 1: "bl", 2: "cis", 3: "es", 4: "e", 5: "fis", 
    6: "gis", 7: "ais", 8: "b", 9: "cisu", 10: "esu", 
    11: "eu", 12: "fisu", 13: "gisu", 14: "aisu", 15: "p" 
    }
Db = {
    0: "r", 1: "des", 2: "es", 3: "f", 4: "fis", 5: "as", 
    6: "bes", 7: "cu", 8: "desu", 9: "esu", 10: "fu", 
    11: "fisu", 12: "asu", 13: "besu", 14: "cuu", 15: "p" 
    }
Eb = {
    0: "r", 1: "es", 2: "f", 3: "g", 4: "as", 5: "bes", 
    6: "cu", 7: "du", 8: "esu", 9: "fu", 10: "gu", 
    11: "asu", 12: "besu", 13: "cuu", 14: "duu", 15: "p" 
    }
Fs = {
    0: "r", 1: "fis", 2: "gis", 3: "bes", 4: "b", 5: "desu", 
    6: "esu", 7: "fu", 8: "fisu", 9: "gisu", 10: "besu", 
    11: "bu", 12: "desuu", 13: "esuu", 14: "fuu", 15: "p" 
    }
Ab = {
    0: "r", 1: "asl", 2: "besl", 3: "c", 4: "des", 5: "es", 
    6: "f", 7: "g", 8: "as", 9: "bes", 10: "cu", 
    11: "desu", 12: "esu", 13: "fu", 14: "gu", 15: "p" 
    }
Bb = {
    0: "r", 1: "besl", 2: "c", 3: "d", 4: "es", 5: "f", 
    6: "g", 7: "a", 8: "bes", 9: "cu", 10: "du", 
    11: "esu", 12: "fu", 13: "gu", 14: "au", 15: "p" 
    }
def translate(individu, anggota_birama, range_nada, tangga_nada):
    def scale(tangga_nada):
        return {
            'C': C,
            'D': D,
            'E': E,
            'F': F,
            'G': G,
            'A': A,
            'B': B,
            'Db': Db,
            'Eb': Eb,
            'Fs': Fs,
            'Ab': Ab,
            'Bb': Bb
        }[tangga_nada]
    tangga_nada = scale(tangga_nada)
    translated = []
    translated_string = ''
    translated_string_list = []
    for i in range(len(individu)):
        r_counter = 0
        j = 0
        p_counter = 0
        while j < anggota_birama:
            if individu[i][j] == 0:
                while j < anggota_birama and individu[i][j] == 0:
                    r_counter+=1
                    j+=1
                if r_counter == 1:
                    translated.append("r")
                else:
                    translated.append("r" + str(r_counter))
                r_counter = 0
            elif individu[i][j] == range_nada:
                p = individu[i][j-1]
                while j < anggota_birama and individu[i][j] == range_nada:
                    p_counter+=1
                    j+=1
                translated.append(tangga_nada[p] + str(p_counter))
                p_counter = 0
            else:
                if j >= anggota_birama:
                    j-=1
                translated.append(tangga_nada[individu[i][j]])
            j+= 1
    
    for i in range(len(translated)):
        if '1' in translated[i]:
            temp = str(translated[i]).replace('1', str(2))
            translated[i] = temp
        elif '2' in translated[i]:
            temp = str(translated[i]).replace('2', str(1))
            translated[i] = temp
        else:
            temp = str(translated[i]) + '4'
            translated[i] = temp
        translated_string += translated[i] + ' '
        # if '1' in translated[i][j] or '2' in translated[i][j] and not duration:
        #     duration = True
        # elif duration and '1' in translated[i][j]:
        #     temp = str(translated[i][j]).replace('1','')
        #     translated[i][j] = temp
        # elif duration and '2' in translated[i][j]:
        #     temp = str(translated[i][j]).replace('1','')
        #     translated[i][j] = temp
        # elif duration and '1' not in translated[i][j] and translated[i][j] != 'r':
        #     temp = translated[i][j] + ','
        #     translated[i][j] = temp
            #     duration = False
    translated_string = str(translated_string).replace('u', "'")
    translated_string = str(translated_string).replace('l', ",")
    return translated_string

# arr = [[ 7.,  3.,  8.,  9.,  4., 13., 11., 12.,  0.,  9.],
#        [ 0., 10.,  8.,  3.,  5., 13.,  2., 11.,  5.,  1.],
#        [ 1., 14.,  5.,  8., 10.,  0.,  8., 15., 15.,  4.],
#        [ 2.,  6.,  9., 15., 14.,  9.,  3.,  7., 14.,  1.],
#        [ 5.,  0., 12.,  8.,  1.,  8.,  9.,  0., 14.,  8.]]
# print(translate(arr, 10, 15, 'E'))