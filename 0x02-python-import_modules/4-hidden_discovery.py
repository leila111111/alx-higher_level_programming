#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hiden_list = dir(hidden_4)
    for name in hiden_list:
        if name[:2] != "__":
            print("{}".format(name))
