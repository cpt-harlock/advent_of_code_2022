#!/usr/bin/python3

import argparse
import numpy as np



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=str)
    args = parser.parse_args()
    input_file = args.input

    char_list = []
    index = 0
    # first part 
    with open(input_file) as f:
        line = f.readline()
        char_list.append(line[0])
        char_list.append(line[1])
        char_list.append(line[2])
        char_list.append(line[3])
        #print(char_list)
        for index in range(4,len(line)):
            if len(set(char_list)) == 4:
                break
            for i in range(3):
                char_list[i] = char_list[i+1]
            char_list[3] = line[index]
    print("First half answer: ", index)

    # second part 
    char_list.clear()
    with open(input_file) as f:
        line = f.readline()
        for jjj in range(14):
            char_list.append(line[jjj])
        for index in range(14,len(line)):
            if len(set(char_list)) == 14:
                break
            for i in range(13):
                char_list[i] = char_list[i+1]
            char_list[13] = line[index]
    print("Second half answer: ",index)
