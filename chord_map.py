C = {
        0: "r", 1: "c", 2: "d:m", 3: "e:m", 4: "f", 5: "g", 
        6: "a:m", 7: "b:dim", 8: "cu", 9: "du:m", 10: "eu:m", 
        11: "fu", 12: "gu", 13: "au:m", 14: "bu:dim", 15: "p" 
    }
D = {
        0: "r", 1: "d", 2: "e:m", 3: "fis:m", 4: "g", 5: "a", 
        6: "b:m", 7: "cis:dim", 8: "du", 9: "eu:m", 10: "fisu:m", 
        11: "gu", 12: "au", 13: "bu:m", 14: "cisu:dim", 15: "p" 
    }
E = {
        0: "r", 1: "e", 2: "fis:m", 3: "gis:m", 4: "a", 5: "b", 
        6: "cis:m", 7: "dis:dim", 8: "eu", 9: "fisu:m", 10: "gisu:m", 
        11: "au", 12: "bu", 13: "cisu:m", 14: "disu:dim", 15: "p" 
    }
F = {
        0: "r", 1: "f", 2: "g:m", 3: "a:m", 4: "bes", 5: "c", 
        6: "d:m", 7: "e:dim", 8: "fu", 9: "gu:m", 10: "au:m", 
        11: "besu", 12: "cu", 13: "du:m", 14: "eu:dim", 15: "p" 
    }
G = {
        0: "r", 1: "g", 2: "a:m", 3: "b:m", 4: "c", 5: "d", 
        6: "e:m", 7: "fis:dim", 8: "gu", 9: "au:m", 10: "bu:m", 
        11: "cu", 12: "du", 13: "eu:m", 14: "fisu:dim", 15: "p" 
    }
A = {
        0: "r", 1: "al", 2: "bl:m", 3: "cis:m", 4: "d", 5: "e", 
        6: "fis:m", 7: "gis:dim", 8: "au", 9: "bu:m", 10: "cisu:m", 
        11: "du", 12: "eu", 13: "fisu:m", 14: "gisu:dim", 15: "p" 
    }
B = {
        0: "r", 1: "bl", 2: "cis:m", 3: "es:m", 4: "e", 5: "fis", 
        6: "gis:m", 7: "ais:dim", 8: "b", 9: "cisu:m", 10: "esu:m", 
        11: "eu", 12: "fisu", 13: "gisu:m", 14: "aisu:dim", 15: "p" 
    }
Db = {
        0: "r", 1: "des", 2: "es:m", 3: "f:m", 4: "fis", 5: "as", 
        6: "bes:m", 7: "cu:dim", 8: "desu", 9: "esu:m", 10: "fu:m", 
        11: "fisu", 12: "asu", 13: "besu:m", 14: "cuu:dim", 15: "p" 
    }
Eb = {
        0: "r", 1: "es", 2: "f:m", 3: "g:m", 4: "as", 5: "bes", 
        6: "cu:m", 7: "du:dim", 8: "esu", 9: "fu:m", 10: "gu:m", 
        11: "asu", 12: "besu", 13: "cuu:m", 14: "duu:dim", 15: "p" 
    }
Fs = {
        0: "r", 1: "fis", 2: "gis:m", 3: "bes:m", 4: "b", 5: "desu", 
        6: "esu:m", 7: "fu:dim", 8: "fisu", 9: "gisu:m", 10: "besu:m", 
        11: "bu", 12: "desuu", 13: "esuu:m", 14: "fuu:dim", 15: "p" 
    }
Ab = {
        0: "r", 1: "asl", 2: "besl:m", 3: "c:m", 4: "des", 5: "es", 
        6: "f:m", 7: "g:dim", 8: "as", 9: "bes:m", 10: "cu:m", 
        11: "desu", 12: "esu", 13: "fu:m", 14: "gu:dim", 15: "p" 
    }
Bb = {
        0: "r", 1: "besl", 2: "c:m", 3: "d:m", 4: "es", 5: "f", 
        6: "g:m", 7: "a:dim", 8: "bes", 9: "cu:m", 10: "du:m", 
        11: "esu", 12: "fu", 13: "gu:m", 14: "au:dim", 15: "p" 
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

    for i in range(len(individu)):
        j = 0
        p_counter = 0
        while j < anggota_birama:
            if j != anggota_birama-1 and individu[i][j+1] == range_nada:
                p = individu[i][j]
                while j < anggota_birama-1 and individu[i][j+1] == range_nada:
                    p_counter+=1
                    j+=1
                if ':' in tangga_nada[p]:
                    chord_split = (tangga_nada[p].split(':'))[0]
                    modifier_split = (tangga_nada[p].split(':'))[1]
                    translated.append(chord_split + str(p_counter) + ':' + modifier_split)
                else:
                    translated.append(tangga_nada[p] + str(p_counter))
                p_counter = 0
            else:
                if j >= anggota_birama:
                    j-=1
                translated.append(tangga_nada[individu[i][j]])
            j+= 1
            # elif individu[i][j] == range_nada:
            #     p = individu[i][j-1]
            #     while j < anggota_birama and individu[i][j] == range_nada:
            #         p_counter+=1
            #         j+=1
            #     if ':' in tangga_nada[p]:
            #         chord_split = (tangga_nada[p].split(':'))[0]
            #         modifier_split = (tangga_nada[p].split(':'))[1]
            #         translated.append(chord_split + str(p_counter) + ':' + modifier_split)
            #     else:
            #         translated.append(tangga_nada[p] + str(p_counter))
            #     p_counter = 0
            # else:
            #     if j >= anggota_birama:
            #         j-=1
            #     translated.append(tangga_nada[individu[i][j]])
            # j+= 1
    for i in range(len(translated)):
        if '1' in translated[i]:
            temp = str(translated[i]).replace('1', str(2))
            translated[i] = temp
        elif '2' in translated[i]:
            temp = str(translated[i]).replace('2', str(1))
            translated[i] = temp
        else:
            if ':' in translated[i]:
                chord_split = (translated[i].split(':'))[0]
                modifier_split = (translated[i].split(':'))[1]
                temp = str(chord_split) + '4' + ':' + modifier_split
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
# print(translate(arr, 10, 15, 'C'))