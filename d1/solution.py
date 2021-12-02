def count_increasing(fname, width=1):
    count = 0
    with open(fname) as f:
        sonar = [int(num) for num in f.readlines()]

    currsum = sum(sonar[:width])
    for idx in range(width, len(sonar)):
        nextsum = currsum - sonar[idx - width] + sonar[idx]
        if nextsum > currsum: count = count + 1
        currsum = nextsum
    
    return count

if __name__ == "__main__":
    assert count_increasing("test_input") == 7
    print("P1:\t" + str(count_increasing("input")))

    assert count_increasing("test_input", 3) == 5
    print("P2:\t" + str(count_increasing("input", 3)))