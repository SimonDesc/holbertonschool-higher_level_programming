#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = "arguments"
    delim = "."
    if len(sys.argv) == 2:
        arg = "argument"
    if len(sys.argv) >= 2:
        delim = ":"

    print("{} {}{}".format(len(sys.argv) - 1, arg, delim))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
