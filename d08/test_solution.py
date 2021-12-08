
import os
import sys
import numpy as np

def FNAME1(signals, outputs):
    valid_counts = set([2, 3, 4, 7])    
    return sum([sum([len(o) in valid_counts for o in output]) for output in outputs])

num2seg = {
    0 : 'abcefg',
    1 : 'cf',
    2 : 'acdeg',
    3 : 'acdfg',
    4 : 'bcdf',
    5 : 'abdfg',
    6 : 'abdefg',
    7 : 'acf', 
    8 : 'abcdefg',
    9 : 'abcdfg'
}

len2num = {
    2 : [1],
    3 : [7],
    4 : [4],
    5 : [2, 3, 5],
    6 : [0, 6, 9],
    7 : [8]
}

def decode(signal, output):
    num = 0
    encode = {}
    decode = {}
    signalset = [set(s) for s in signal]
    signal = [''.join(sorted(s)) for s in signal]
    assert len(set(signal)) <= 10
    ls = [len(s) for s in signal]
    output = [''.join(sorted(o)) for o in output]
    lo = [len(o) for o in output]
    # segments = set('abcdefg')

    for clen in [2, 3, 4, 7]:
        if clen in ls: 
            index = ls.index(clen)
            encode[len2num[clen][0]] = signal[index]
            decode[signal[index]] = len2num[clen][0]
    
    for idx, s in enumerate(signal):
        bd = set(encode[4]) - set(encode[1])
        if ls[idx] == 5:
            
            if set(encode[1]).issubset(set(s)):
                encode[3] = s
                decode[s] = 3
            elif bd.issubset(set(s)):
                encode[5] = s
                decode[s] = 5
            else:
                encode[2] = s
                decode[s] = 2
        if ls[idx] == 6:
            if  bd.issubset(set(s)):
                if set(encode[1]).issubset(set(s)):
                    encode[9] = s
                    decode[s] = 9
                else:
                    encode[6] = s
                    decode[s] = 6
            else:
                encode[0] = s
                decode[s] = 0

    not_in_encode = [1 if x not in encode else 0 for x in range(10)]
    assert sum(not_in_encode) <= 1
    if sum(not_in_encode): not_in_encode = not_in_encode.index(1)
    else: not_in_encode = None

    outnum = []    
    for o in output:
        if o in decode: outnum.append(decode[o])
        else: outnum.append(not_in_encode)
   
    return sum([pow(10, 3-i)*outnum[i] for i in range(4)])


def FNAME2(signals, outputs):   
    outnums = [decode(signals[i], outputs[i]) for i in range(len(signals))] 
    # print(outnums)
    return sum(outnums)

def preprocess(fname):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    with open(fpath) as f:
        arr = f.readlines()
    signals = [line.split('|')[0] for line in arr]
    outputs = [line.split('|')[1][:-1] for line in arr]
    signals = [s.split() for s in signals]
    outputs = [o.split() for o in outputs]
    return signals, outputs


def test_day8(outfile):

    test_signals, test_outputs = preprocess("test_input")
    signals, outputs = preprocess("input")


    if outfile:
        log = open(outfile, 'a')
        sys.stdout = log  
        header = '## '
        codeblock = '\n```'
    else:
        header = ''
        codeblock = ''

    print(header + "Day 8 Results:" + codeblock)

    assert FNAME1(test_signals, test_outputs) == 26
    print("P1:\t" + str(FNAME1(signals, outputs)))

    assert FNAME2(test_signals, test_outputs) == 61229
    print("P2:\t" + str(FNAME2(signals, outputs)) + codeblock)

if __name__ == "__main__":
    test_day8(None)