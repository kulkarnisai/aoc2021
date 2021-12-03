
import os
import sys
import ctypes
import numpy as np

def gamma_and_epsilon(arr):
    count = np.sum(arr,  axis=0)
    thresh = len(arr)//2 if len(arr) % 2 == 0 else len(arr)//2 + 1
    gamma = [1 if x >= thresh else 0 for x in count]
    epsilon = [0 if x >= thresh else 1 for x in count]
    return gamma, epsilon

def gamma_times_epsilon(arr): 
    gamma, epsilon = gamma_and_epsilon(arr)
    gamma = int(''.join([str(dig) for dig in gamma]), 2)
    epsilon = int(''.join([str(dig) for dig in epsilon]), 2)
    return gamma*epsilon

def o2_and_co2(arr):
    o2 = np.copy(arr)
    idx = 0
    while o2.shape[0] > 1 and idx < o2.shape[1]:
        gamma, _ = gamma_and_epsilon(o2)
        o2 = o2[o2[:, idx] == gamma[idx]]
        idx = idx + 1

   
    co2 = np.copy(arr)
    idx = 0
    while co2.shape[0] > 1 and idx < co2.shape[1]:
        _, epsilon = gamma_and_epsilon(co2)
        co2 = co2[co2[:, idx] == epsilon[idx]]
        idx = idx + 1
    return o2[0], co2[0]
    

def life_support_rating(arr): 
    o2, co2 = o2_and_co2(arr)
    o2_rating = int(''.join([str(dig) for dig in o2]), 2)
    co2_rating = int(''.join([str(dig) for dig in co2]), 2)
    return o2_rating * co2_rating

def preprocess(fname):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    with open(fpath) as f:
        arr = [[ int(letter) for letter in line[:-1]] for line in f.readlines()]
    return np.array(arr)

def test_dayN(outfile):

    test_arr = preprocess("test_input")
    arr = preprocess("input")

    if outfile:
        log = open(outfile, 'a')
        sys.stdout = log  
        header = '## '
        codeblock = '\n```'
    else:
        header = ''
        codeblock = ''

    print(header + "Day 3 Results:" + codeblock)

    assert gamma_times_epsilon(test_arr) == 198
    print("P1:\t" + str(gamma_times_epsilon(arr)))

    assert life_support_rating(test_arr) == 230
    print("P2:\t" + str(life_support_rating(arr)) + codeblock)

if __name__ == "__main__":
    test_dayN(None)