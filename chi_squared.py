"""
want to do statistical tests to prove this is random
"""
import csv
from scipy.stats import chisquare
from collections import Counter

        
pends = 8
Sec = 30000

def chi_square():
    nums = []
    with open(f'{pends}P-{Sec}Sec3.csv', 'r') as file:
        reader = csv.reader(file)
        for n in reader:
            nums.append(int(n[0]))

    numCount = Counter(nums)
    expectedFreq = len(nums) / 2**pends

    observed_freq = [numCount[num] for num in range(2**pends)]
    frequencies = [expectedFreq] * 2**pends

    chi_sqared, p_val = chisquare(observed_freq, f_exp=frequencies)


    total = 0
    for i in range(2**pends):
        diff = (observed_freq[i] - expectedFreq)**2
        diff /= expectedFreq
        total += diff
    
    print(total)
    return chi_sqared, p_val
#minimum distance test

    



print(chi_square())

