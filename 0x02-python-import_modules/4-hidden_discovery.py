#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    name_arr = dir(hidden_4)
    arr_len = len(name_arr)

    for name in name_arr:
        if (name[:2] != "__"):
            print(name)
