#!/usr/bin/python3
import argparse

def subset(x,y):
    ret_1 = True
    ret_2 = True
    for i in x:
        if i not in y:
            ret_1 = False
    for i in y:
        if i not in x:
            ret_2 = False
    return ret_1 or ret_2

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=str)
    args = parser.parse_args()
    input_file = args.input
    subset_counter = 0
    overlap_counter = 0
    with open(input_file) as f:
        for line in f.readlines():
            if line == "\n":
                continue
            rec = line.split(",")
            first_range = rec[0]
            second_range = rec[1]
            first_range = first_range.split("-")
            second_range = second_range.split("-")
            first_range = range(int(first_range[0]), int(first_range[1])+1)
            second_range= range(int(second_range[0]), int(second_range[1])+1)
            intersection = [ v for v in first_range if v in second_range ]
            if subset(first_range, second_range):
                subset_counter += 1
            if len(intersection) > 0:
                overlap_counter += 1
    print("First half answer:  ", subset_counter)
    print("Second half answer:  ", overlap_counter)
