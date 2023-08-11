#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    argv = sys.argv
    print(argv[2])
    num_argv = (len(argv) - 1)
    if num_argv < 3:
        print("usage: ./100-my_calculator.py <a> <operator> <b>")
    elif num_argv > 3:
        print(f"hello {num_argv}")
        for arg in argv:
            print(arg)
        sys.exit(1)
    elif num_argv == 3:
        for arg in argv:
            print(arg)
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+":
            print("{} {} {} = {}".format(a, argv[2], b, add(a, b)))
        elif argv[2] == "-":
            print("{} {} {} = {}".format(a, argv[2], b, sub(a, b)))
        elif argv[2] == "*":
            print("{} {} {} = {}".format(a, argv[2], b, mul(a, b)))
        elif argv[2] == "/":
            print("{} {} {} = {}".format(a, argv[2], b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
