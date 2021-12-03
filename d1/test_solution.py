import os
import sys

def count_increasing(sonar, width=1):
    count = 0

    currsum = sum(sonar[:width])
    for idx in range(width, len(sonar)):
        nextsum = currsum - sonar[idx - width] + sonar[idx]
        if nextsum > currsum: count = count + 1
        currsum = nextsum
    
    return count

# if __name__ == "__main__":
#     assert count_increasing("test_input") == 7
#     print("P1:\t" + str(count_increasing("input")))

#     assert count_increasing("test_input", 3) == 5
#     print("P2:\t" + str(count_increasing("input", 3)))

def preprocess(fname):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    with open(fpath) as f:
        arr = [int(num) for num in f.readlines()]

    return arr

def test_day1(outfile):

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

    print(header + "Day 1 Results:" + codeblock)

    assert count_increasing(test_arr) == 7
    print("P1:\t" + str(count_increasing(arr)))

    assert count_increasing(test_arr, 3) == 5
    print("P2:\t" + str(count_increasing(arr, 3)) + codeblock)

if __name__ == "__main__":
    test_day1(None)