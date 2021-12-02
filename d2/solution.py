def get_position(fname):
    x, y = 0, 0
    with open(fname) as f:
        commands = [ line.split(' ') for line in f.readlines()]
    for command in commands:
        if command[0] == "forward":
            x = x + int(command[1])
        elif command[0] == "down":
            y = y + int(command[1])
        else:
            y = y - int(command[1])
    
    return x * y

def get_position_with_aim(fname):
    x, y, aim = 0, 0, 0
    with open(fname) as f:
        commands = [ line.split(' ') for line in f.readlines()]

    for command in commands:
        if command[0] == "forward":
            x = x + int(command[1])
            y = y + aim*int(command[1])
        elif command[0] == "down":
            aim = aim + int(command[1])
        else:
            aim = aim - int(command[1])
    
    return x * y

if __name__ == "__main__":
    assert get_position("test_input") == 150
    print("P1:\t" + str(get_position("input")))

    assert get_position_with_aim("test_input") == 900
    print("P2:\t" + str(get_position_with_aim("input")))