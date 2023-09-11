#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    count = 0
    for i in my_list:
        if count == idx:
            my_list.remove(i)
        count += 1
    return my_list
