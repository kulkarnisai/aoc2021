
import os

def get_position(commands):
    x, y = 0, 0
    for command in commands:
        if command[0] == "forward":
            x = x + int(command[1])
        elif command[0] == "down":
            y = y + int(command[1])
        else:
            y = y - int(command[1])
    
    return x * y

def get_position_with_aim(commands):
    x, y, aim = 0, 0, 0
   
    for command in commands:
        if command[0] == "forward":
            x = x + int(command[1])
            y = y + aim*int(command[1])
        elif command[0] == "down":
            aim = aim + int(command[1])
        else:
            aim = aim - int(command[1])
    
    return x * y


def preprocess(fname):
    fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    with open(fpath) as f:
        arr = [ line.split(' ') for line in f.readlines()]
    return arr

def test_day2(outfile=None):

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

    print(header + "Day 2 Results:" + codeblock)

    assert get_position(test_arr) == 150
    print("P1:\t" + str(get_position(arr)))

    assert get_position_with_aim(test_arr) == 900
    print("P2:\t" + str(get_position_with_aim(arr)) + codeblock)

if __name__ == "__main__":
    test_day2()