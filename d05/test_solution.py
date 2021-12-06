
import os
import sys
import re
import math
import numpy as np

def FNAME1(arr, gridsize):
    grid = np.zeros(gridsize)
    for line in arr:
        if line.get_slope()[0] * line.get_slope()[1] == 0:
            for point in line.get_all_points():
                grid[point[0]][point[1]] = grid[point[0]][point[1]] + 1
    # print(grid)
    # print(np.sum(grid >= 2))
    return np.sum(grid >= 2)


def FNAME2(arr, gridsize):    
    grid = np.zeros(gridsize)
    for line in arr:
        for point in line.get_all_points():
            grid[point[0]][point[1]] = grid[point[0]][point[1]] + 1
    # print(grid)
    # print(np.sum(grid >= 2))
    return np.sum(grid >= 2)

class Line:   
    def __init__(self, points):
        points.sort()
        self.x1 = points[0][0]
        self.y1 = points[0][1]
        self.x2 = points[1][0]
        self.y2 = points[1][1]

    def get_slope(self):
        ydelta, xdelta = self.y2 - self.y1, self.x2 - self.x1
        if ydelta == 0: return [1, 0]
        if xdelta == 0: return [0, 1]
        gcd = math.gcd(xdelta, ydelta)
        return [xdelta//gcd, ydelta//gcd]
    
    def get_all_points(self):
        [xdelta, ydelta] = self.get_slope()
        if xdelta == 0: numpoints = (self.y2 - self.y1) 
        else: numpoints = (self.x2 - self.x1)//xdelta 
        return [[self.x1 + i*xdelta, self.y1 + i*ydelta] for i in range(numpoints + 1)]

def preprocess(fname):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    linere = re.compile(r"(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)")
    gridsize = [0, 0]

    def make_line(line):
        match = linere.match(line)
        x1, y1 = int(match.group('x1')), int(match.group('y1'))
        x2, y2 = int(match.group('x2')), int(match.group('y2'))
        gridsize[0] = max(gridsize[0], x1+1, x2+1)
        gridsize[1] = max(gridsize[1], y1+1, y2+1)
        return Line([[x1, y1], [x2, y2]])
 
    with open(fpath) as f:
        arr = [make_line(line) for line in f.readlines()]

    return arr, gridsize



def test_day5(outfile):

    test_arr, test_gridsize = preprocess("test_input")
    arr, gridsize = preprocess("input")

    if outfile:
        log = open(outfile, 'a')
        sys.stdout = log  
        header = '## '
        codeblock = '\n```'
    else:
        header = ''
        codeblock = ''

    print(header + "Day 5 Results:" + codeblock)

    assert FNAME1(test_arr, test_gridsize) == 5
    print("P1:\t" + str(FNAME1(arr, gridsize)))

    assert FNAME2(test_arr, test_gridsize) == 12
    print("P2:\t" + str(FNAME2(arr, gridsize)) + codeblock)

if __name__ == "__main__":
    test_day5(None)