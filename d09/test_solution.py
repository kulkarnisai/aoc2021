
import os
import sys
import numpy as np
import cv2



def FNAME1(arr):    
    arr = arr + 1
    lp = np.full(arr.shape, True)
    lp[1:, :] = np.logical_and(lp[1:, :], (arr[1:, :] < arr[:-1, :]))
    lp[:-1, :] = np.logical_and(lp[:-1, :], (arr[:-1, :] < arr[1:, :]))
    lp[:, 1:] = np.logical_and(lp[:, 1:], (arr[:, 1:] < arr[:, :-1]))
    lp[:, :-1] = np.logical_and(lp[:, :-1],  (arr[:, :-1] < arr[:, 1:]))
    return np.sum(arr[lp]), lp

def get_basin_area(arr, r, c):
    q = [[r, c]]
    visited = np.zeros(arr.shape)
    ba = 0

    def visit(r, c):
        visited[r, c] = 1
        if r > 0 and arr[r-1, c]: q.append([r-1, c])
        if r < arr.shape[0] - 1 and arr[r+1, c]: q.append([r+1, c])
        if c > 0 and arr[r, c-1]: q.append([r, c-1])
        if c < arr.shape[1] - 1 and arr[r, c+1]: q.append([r, c+1])

    while q:
        [r, c] = q.pop()
        if not visited[r, c]:
            visit(r, c)
            ba = ba + 1
    return ba

def FNAME2(arr):   
    bas = []
    _, lp = FNAME1(arr)
    arr = arr != 9
    for r in range(arr.shape[0]):
        for c in range(arr.shape[1]):
            if lp[r][c]:
                bas.append(get_basin_area(arr, r, c))
                
    bas.sort(reverse=True)
    return bas[0]*bas[1]*bas[2]


def preprocess(fname):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    with open(fpath) as f:
        arr = np.array([[int(c) for c in s[:-1]] for s in f.readlines()])
    return arr


def test_day9(outfile):

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

    print(header + "Day 9 Results:" + codeblock)

    assert FNAME1(test_arr)[0] == 15
    print("P1:\t" + str(FNAME1(arr)[0]))

    assert FNAME2(test_arr) == 1134
    print("P2:\t" + str(FNAME2(arr)) + codeblock)

if __name__ == "__main__":
    test_day9(None)