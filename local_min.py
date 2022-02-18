#!/usr/bin/python

import sys

def local_min(matrix):
    file = open(matrix,'r')
    matrix = []
    for i in file.readlines(): ###make matrix
        matrix.append(i.rstrip())
    cout_loc_min = 0
    sum_loc_min = 0
    for x_len in range(len(matrix)):
        for y_len in range(len(matrix[x_len])):
                if x_len == 0: ##top
                    if y_len == 0: ##top_left_corner
                        neigh=(matrix[x_len][y_len],matrix[x_len][y_len+1],matrix[x_len+1][y_len])
                    elif y_len == len(matrix[x_len])-1:##top_right_corner
                        neigh=(matrix[x_len][y_len],matrix[x_len][y_len-1],matrix[x_len+1][y_len])
                    else:
                        neigh=(matrix[x_len][y_len],matrix[x_len][y_len-1],matrix[x_len][y_len+1],matrix[x_len+1][y_len])
                elif x_len == len(matrix[x_len])-1:##bottom
                    if y_len == 0: ##bottom_left_corner
                        neigh=(matrix[x_len][y_len],matrix[x_len-1][y_len],matrix[x_len][y_len+1])
                    elif y_len == len(matrix[x_len])-1: ##bottom_right_corner
                        neigh=(matrix[x_len][y_len],matrix[x_len][y_len-1],matrix[x_len-1][y_len])
                    else:
                        neigh=(matrix[x_len][y_len],matrix[x_len][y_len-1],matrix[x_len-1][y_len],matrix[x_len][y_len+1])
                else:
                    if y_len == 0: ##left
                        neigh=(matrix[x_len][y_len],matrix[x_len-1][y_len],matrix[x_len][y_len+1],matrix[x_len+1][y_len])
                    elif y_len == len(matrix[x_len])-1: ##right
                        neigh=(matrix[x_len][y_len],matrix[x_len][y_len-1],matrix[x_len-1][y_len],matrix[x_len+1][y_len])
                    else: ##other_all_position
                        neigh=(matrix[x_len][y_len],matrix[x_len][y_len-1],matrix[x_len-1][y_len],matrix[x_len][y_len+1],matrix[x_len+1][y_len])
                if min(neigh) == matrix[x_len][y_len]: ##check local minima
                    cout_loc_min += 1
                    sum_loc_min += int(matrix[x_len][y_len])
    print(str(cout_loc_min),"/",str(sum_loc_min))

def main():
    if len(sys.argv) < 2:
        print("ex) python local_min.py [matrix file]")
    else:
        local_min(sys.argv[1])

if __name__ == "__main__": main()