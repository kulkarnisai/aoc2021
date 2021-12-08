
import os
import sys
import numpy as np
from scipy.optimize import minimize


def FNAME1(arr):    
    med = int(np.median(arr))
    return np.sum(np.abs(arr - med))

def total_fuel(arr, y):
    def fuel(x, y):
        delta = abs(x-y)
        return delta*(delta+1)//2
    return np.sum([fuel(num, y) for num in arr])

def FNAME2(arr):    
    minval, maxval = np.min(arr), np.max(arr)
    min_fuel = float('inf')
    for guess in range(minval, maxval+1):
        fuel = total_fuel(arr, guess)
        # print(guess, fuel)
        if fuel < min_fuel:
            min_fuel = fuel
    return min_fuel

def preprocess(fname):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    with open(fpath) as f:
        line = f.readline()
    arr = np.array([int(num) for num in line.split(',')])
    return arr


def test_day7(outfile):

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

    print(header + "Day 7 Results:" + codeblock)

    assert FNAME1(test_arr) == 37
    print("P1:\t" + str(FNAME1(arr)))

    assert FNAME2(test_arr) == 168
    print("P2:\t" + str(FNAME2(arr)) + codeblock)

if __name__ == "__main__":
    test_day7(None)