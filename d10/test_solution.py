
import os
import sys
import numpy as np

pairs = {
    '}' : '{',
    ']' : '[',
    ')' : '(',
    '>' : '<'
}

scores1 = {
    '}': 1197,
    ')': 3,
    ']': 57,
    '>': 25137,
}



def get_first_illegal(line):
    stack = []
    for char in line:
        if char in pairs:
            if stack and stack.pop() == pairs[char]:
                continue
            else:
                return char, None
        else:
            stack.append(char)
    return None, stack

def FNAME1(arr):    
    score = 0
    for line in arr:
        char = get_first_illegal(line)[0]
        if char: score = score + scores1[char]
    return score


scores2 = {
    '{': 3,
    '(': 1,
    '[': 2,
    '<': 4,
}
reverse_pair = {
    '{': '}',
    '(': ')',
    '[': ']',
    '<': '>',
}

def completion_score(stack):
    linescore = 0
    while stack:
        char = stack.pop()
        linescore = linescore*5 + scores2[char]
    return linescore


def FNAME2(arr):   
    scores = []
    for line in arr:
        illegal, stack = get_first_illegal(line)
        if illegal:
            continue
        else:
            scores.append(completion_score(stack))
    return np.median(scores)
    
def preprocess(fname):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    with open(fpath) as f:
        arr = [line[:-1] for line in f.readlines()]
    return arr


def test_day10(outfile):

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

    print(header + "Day 10 Results:" + codeblock)

    assert FNAME1(test_arr) == 26397
    print("P1:\t" + str(FNAME1(arr)))

    assert FNAME2(test_arr) == 288957
    print("P2:\t" + str(FNAME2(arr)) + codeblock)

if __name__ == "__main__":
    test_day10(None)