#!/usr/bin/python3

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    args = parser.parse_args()
    f_input = args.input
    priority_dict = {}
    list_of_shared_prio = []
    for x in range(65,91):
        priority_dict[chr(x)] = (x % 65) + 27
    for x in range(97,123):
        priority_dict[chr(x)] = (x % 96)
    # FIRST PART
    with open(f_input) as f:
        for j,line in enumerate(f.readlines()):
            line = line.strip('\n')
            first_half = []
            second_half = []
            length = len(line)
            for i,c in enumerate(line):
                if (i < length/2):
                    first_half.append(c)
                else:
                    second_half.append(c)
            #print(j)
            #print(first_half)
            #print(second_half)
            intersection = [ v for v in first_half if v in second_half]
            # should be one element
            #print(intersection)
            #print(priority_dict[intersection[0]])
            list_of_shared_prio.append(priority_dict[intersection[0]])
    print("First half answer: ", sum(list_of_shared_prio))
    # SECOND PART
    group = []
    list_of_badges_values = []
    with open(f_input) as f:
        for j,line in enumerate(f.readlines()):
            line = line.strip('\n')
            group.append(line)
            # if last member
            if j % 3 == 2:
                intersection = [ v for v in group[0] if v in group[1] ]
                intersection = [ v for v in intersection if v in group[2]]
                list_of_badges_values.append(priority_dict[intersection[0]])
                group.clear()
    print("Second half answer: ", sum(list_of_badges_values))

