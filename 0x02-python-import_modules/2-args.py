#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    num_args = len(argv)
    if num_args > 2:
        print(f"{num_args - 1} arguments:")
        for index, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(index, arg))
    elif num_args == 2:
        print("{} argument:\n{}: {}".format(num_args - 1, num_args - 1, argv[1]))
    else:
        print("{} arguments.".format(num_args - 1))
