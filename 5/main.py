#!/usr/bin/python3

import argparse
import numpy as np

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=str)
    args = parser.parse_args()
    input_file = args.input

    stack_dict = {}
    parsing_stacks = False

    # first part 
    with open(input_file) as f:
        for i, line in enumerate(f.readlines()):
            if line == "\n":
                parsing_stacks = not parsing_stacks
                continue
            if parsing_stacks:
                if not '[' in line:
                    continue
                #print(i, line)
                index = 1
                space_counter = 0
                parsing_lett = False
                for c in line:
                    if c == ' ':
                        space_counter += 1
                        continue
                    if c == '[':
                        parsing_lett = True
                        continue
                    if c == ']':
                        parsing_lett = False
                        continue
                    if parsing_lett:
                        if space_counter != 0:
                            if space_counter == 1:
                                index = index + 1
                            else:
                                index = index + np.ceil(space_counter/4)
                        #print(c, index, space_counter)
                        if stack_dict.get(index) == None:
                            stack_dict[index] = [c]
                        else:
                            stack_dict[index].insert(0,c)
                        space_counter = 0
            if not parsing_stacks:
                rec = line.split(" ")
                amount = int(rec[1])
                source = int(rec[3])
                dest = int(rec[5])
                for j in range(amount):
                    temp = stack_dict[source].pop()
                    stack_dict[dest].append(temp)

    print("first half")
    for key in sorted(stack_dict.keys()):
        print("{}".format(stack_dict[key].pop()))

    # second part
    stack_dict = {}
    parsing_stacks = False

    # first part 
    with open(input_file) as f:
        for i, line in enumerate(f.readlines()):
            if line == "\n":
                parsing_stacks = not parsing_stacks
                continue
            if parsing_stacks:
                if not '[' in line:
                    continue
                #print(i, line)
                index = 1
                space_counter = 0
                parsing_lett = False
                for c in line:
                    if c == ' ':
                        space_counter += 1
                        continue
                    if c == '[':
                        parsing_lett = True
                        continue
                    if c == ']':
                        parsing_lett = False
                        continue
                    if parsing_lett:
                        if space_counter != 0:
                            if space_counter == 1:
                                index = index + 1
                            else:
                                index = index + np.ceil(space_counter/4)
                        #print(c, index, space_counter)
                        if stack_dict.get(index) == None:
                            stack_dict[index] = [c]
                        else:
                            stack_dict[index].insert(0,c)
                        space_counter = 0
            if not parsing_stacks:
                rec = line.split(" ")
                amount = int(rec[1])
                source = int(rec[3])
                dest = int(rec[5])
                temp_list = []
                for j in range(amount):
                    temp = stack_dict[source].pop()
                    temp_list.append(temp)
                temp_list = reversed(temp_list)
                for el in temp_list:
                    stack_dict[dest].append(el)


    print("second half")
    for key in sorted(stack_dict.keys()):
        print("{}".format(stack_dict[key].pop()))
