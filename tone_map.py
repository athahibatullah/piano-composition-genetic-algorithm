C = {0: "r", 1: "c", 2: "d", 3: "e", 4: "f", 5: "g", 
    6: "a", 7: "b", 8: "c'", 9: "d'", 10: "e'", 
    11: "f'", 12: "g'", 13: "a'", 14: "b'", 15: "p" }

def translate(individu, anggota_birama, range_nada):
    translated = []
    for i in range(len(individu)):
        r_counter = 0
        j = 0
        p_counter = 0
        # for j in range(anggota_birama):
            # translated.append(C[individu[i][j]])
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
                print(i,j,individu[i][j])
                p = individu[i][j-1]
                while j < anggota_birama and individu[i][j] == range_nada:
                    p_counter+=1
                    j+=1
                translated.append(C[p] + str(p_counter))
                p_counter = 0
            else:
                if j >= anggota_birama:
                    j-=1
                translated.append(C[individu[i][j]])
            j+= 1
    return translated
    
# arr = [[ 8.,  3., 10., 13.,  3.,  1., 10.,  0.,  3.,  6.],
#        [ 7.,  8.,  6., 12., 11.,  9., 13.,  7., 11.,  7.],
#        [13.,  3., 14.,  7., 10.,  6.,  3.,  0.,  7.,  8.],
#        [ 1.,  4., 15.,  15., 12.,  5., 11., 13., 14.,  0.],
#        [ 3., 14., 11., 15.,  5.,  1.,  7., 13., 14.,  15.]]
# print(translate(arr, 10, 15))