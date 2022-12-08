#!/usr/bin/python3
import argparse

class Node:

    def __init__(self, name, is_dir, size):
        self.name = name
        self.is_dir = is_dir
        self.size = size
        self.list_of_children = []
        

    def add_child(self, name, is_dir, size):
        self.list_of_children.append(Node(name, is_dir, size))

    def get_size(self):
        temp = 0
        for d in self.list_of_children:
            temp += d.get_size()
        return temp + self.size

    def find_child(self, name):
        ret = None
        if self.name == name:
            ret = self
        if ret == None and self.is_dir:
            new_name = "/".join((name.split("/")[1:]))
            for n in self.list_of_children:
                if new_name.split("/")[0] == n.name:
                    ret = n.find_child(new_name)
                    if ret != None:
                        break
        return ret

    def print_tree(self, tab_level=0):
        tab_string = '|---|'*tab_level
        print(tab_string, self.name, self.get_size())
        for c in self.list_of_children:
            c.print_tree(tab_level+1)

    def print_if_dir_size(self, required_size, tab_level=0):
        tab_string = '|---|'*tab_level
        if self.is_dir and self.get_size() <= required_size:
            print(tab_string, self.name, self.get_size())
        for c in self.list_of_children:
            c.print_if_dir_size(required_size,tab_level+1)

    def print_if_freeing_up_enough_space(self, total_space, occupied_space, required_space):
        if self.is_dir and  total_space-(occupied_space-self.get_size()) >= required_space:
            print(self.name, self.get_size())
        for c in self.list_of_children:
            c.print_if_freeing_up_enough_space(total_space, occupied_space, required_space)



root_node = Node(name="", is_dir=True, size=0)







if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    args = parser.parse_args()
    input_file = args.input

    actual_dir_name = ""

    with open(input_file) as f:
        ls_line = False
        for i,line in enumerate(f.readlines()):
            rec = line.split(" ")
            for i in range(len(rec)):
                rec[i] = rec[i].strip('\n')
            # command
            if rec[0] == "$":
                # ls command
                if rec[1] == "ls":
                    #print(rec)
                    ls_line = True
                    continue
                # cd command 
                if rec[1] == "cd":
                    ls_line = False
                    rec[2] = rec[2].strip("\n")
                    #print(rec)
                    #print(rec)
                    # change dir
                    if rec[2] == "/":
                        actual_dir_name = ""
                    elif rec[2] == "..":
                        actual_dir_name = "/".join(((actual_dir_name.split("/"))[:-1]))
                    else:
                        actual_dir_name = actual_dir_name + "/" + rec[2]
                    #print(actual_dir_name)
            if ls_line:
                type_or_size = rec[0]
                file_name = rec[1]
                node = root_node.find_child(actual_dir_name)
                #print(node.name)
                if type_or_size == "dir":
                    node.add_child(file_name, True, 0)
                else:
                    node.add_child(file_name, False, int(type_or_size))


        #root_node.print_tree(0)
        #root_node.print_if_dir_size(100000,0)
        root_node.print_if_freeing_up_enough_space(70000000,42586708,30000000)


                    
                


