import numpy as np
import parameter_fitness as pf
import random

def inisialisasi_individu(banyak_birama, anggota_birama, range_nada, komposisi):
    alt_nums_core = []
    for i in range(banyak_birama):
        alt_nums = []
        randnums = []
        sama = -1
        for j in range(anggota_birama):
            num = random.randint(0,range_nada-1)
            alt_nums.append(num)
            if j == 0:
                randnums.append(num)
            elif randnums[j-1] == num:
                randnums.append(range_nada)
                sama = num
            elif num == sama:
                randnums.append(range_nada)
            elif num != sama:
                randnums.append(num)
                sama = -1
            else:
                randnums.append(num)
        # quota = 15
        # while quota > 0:
        #     if quota == 15:
        #         num = random.randint(0,14)
        #     else:
        #         num = random.randint(0,15)

        #     if num == 15:
        #         banyak_random = random.randint(1,quota) 
        #         for j in range(banyak_random):
        #             randnums.append(15)
        #         quota -= banyak_random
        #     else:
        #         randnums.append(num)
        #         quota -= 1
        alt_nums_core.append(alt_nums)
        komposisi[i] = np.array(randnums)
    return komposisi, np.array(alt_nums_core)