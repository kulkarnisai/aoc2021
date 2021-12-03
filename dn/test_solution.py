
import os
import sys
def FNAME1(arr):    
   return 0


def FNAME2(arr):    
   return 0

def preprocess(fname):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    with open(fpath) as f:
        arr = f.readlines()

    return arr

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

    print(header + "Day N Results:" + codeblock)

    assert FNAME1(test_arr) == 0
    print("P1:\t" + str(FNAME1(arr)))

    assert FNAME2(test_arr) == 0
    print("P2:\t" + str(FNAME2(arr)) + codeblock)

if __name__ == "__main__":
    test_dayN(None)