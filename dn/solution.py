def FNAME1(fname):    
    with open(fname) as f:
        inarr = f.readlines()


def FNAME2(fname):    
    with open(fname) as f:
        inarr = f.readlines()


if __name__ == "__main__":
    assert FNAME1("test_input") == ANS1
    print("P1:\t" + str(FNAME1("input")))

    assert FNAME2("test_input", 3) == ANS2
    print("P2:\t" + str(FNAME2("input", 3)))