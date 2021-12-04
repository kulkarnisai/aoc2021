
import os
import sys
import numpy as np

def get_score(seq, board):
    def wins(visited):
        for row in visited:
            if all(row): 
                return True
        visited = np.transpose(visited)
        for row in visited:
            if all(row):
                return True
        return False

    winidx = sys.maxsize
    score = 0
    visited = np.zeros(board.shape, dtype=np.uint8)

    for idx, num in enumerate(seq):
        visited[board == num] = 1
        if wins(visited):
            winidx = idx
            score = np.sum(board[visited == 0]) * seq[winidx]            
            # print(visited)
            # print(winidx, score)
            return winidx, score
    return winidx, score


def winning_board_score(seq, boards):    
    minwinidx = sys.maxsize
    winscore = 0
    for board in boards:
        winidx, score = get_score(seq, board)
        if winidx < minwinidx:
            minwinidx = winidx
            winscore = score
        
    return winscore


def losing_board_score(seq, boards): 
    maxwinidx = -1
    winscore = 0
    for board in boards:
        winidx, score = get_score(seq, board)
        if winidx > maxwinidx:
            maxwinidx = winidx
            winscore = score
        
    return winscore

def preprocess(fname):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    with open(fpath) as f:
        arr = f.readlines()
    sequence = np.array([int(num) for num in arr[0].split(',') if num])
    boardsize = 5
    boards = []
    currboard = []
        
    for row in arr[2:]:
        if len(row) >= boardsize:
            currboard.append([int(num) for num in row.split(' ') if num])
        else: 
            boards.append(currboard)
            currboard = []
    # print(sequence)
    for number, board in enumerate(boards):
        try:
            assert len(board) == boardsize
            assert all([len(board[i]) == boardsize for i in range(boardsize)])
        except:
            print(number)
            print(board)

    return sequence, np.array(boards)


def test_day4(outfile):

    test_seq, test_boards = preprocess("test_input")
    seq, boards = preprocess("input")

    if outfile:
        log = open(outfile, 'a')
        sys.stdout = log  
        header = '## '
        codeblock = '\n```'
    else:
        header = ''
        codeblock = ''

    print(header + "Day 4 Results:" + codeblock)

    assert winning_board_score(test_seq, test_boards) == 4512
    print("P1:\t" + str(winning_board_score(seq, boards)))

    assert losing_board_score(test_seq, test_boards) == 1924
    print("P2:\t" + str(losing_board_score(seq, boards)) + codeblock)

if __name__ == "__main__":
    test_day4(None)