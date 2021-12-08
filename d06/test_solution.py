
import os
import sys
from typing import Counter
import numpy as np
from collections import Counter


def FNAME1(arr, ndays): 
    for _ in range(ndays):
        arr = arr - 1
        old_fish = arr.shape[0]
        new_fish = np.sum(arr < 0)
        arr.resize(old_fish + new_fish)
        arr[arr<0] = 6
        arr[old_fish:] = 8
    return arr.shape[0]


def FNAME2(arr, ndays):     
    counts = Counter(arr)
    next9 = [counts[i] for i in range(9)]

    for _ in range(ndays):
        next9[7] = next9[7] + next9[0]
        next9 = next9[1:] + next9[:1]
    return sum(next9)

def preprocess(fname):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    with open(fpath) as f:
        line = f.readline()
    arr = np.array([int(num) for num in line.split(',')])
    return arr


def test_day6(outfile):

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

    print(header + "Day 6 Results:" + codeblock)

    assert FNAME1(test_arr, 18) == 26
    assert FNAME1(test_arr, 80) == 5934
    print("P1:\t" + str(FNAME1(arr, 80)))

    assert FNAME2(test_arr, 18) == 26
    print("P2:\t" + str(FNAME2(arr, 256)) + codeblock)

if __name__ == "__main__":
    test_day6(None)