#!/usr/bin/python3



def read_file(filename=""):
    """read file utf8 con with """
    with open(filename, encoding='UTF-8') as f:
        for line in f:
            print(line, end='')
