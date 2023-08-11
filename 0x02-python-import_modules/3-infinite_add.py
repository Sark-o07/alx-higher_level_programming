#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv
    num_args = len(argv)
    total = 0
    if num_args > 1:
        for _, arg in enumerate(argv[1:]):
            total += int(arg)
    print(total)
