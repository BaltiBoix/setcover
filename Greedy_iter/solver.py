#!/usr/bin/python
# -*- coding: utf-8 -*-

# The MIT License (MIT)
#
# Copyright (c) 2014 Carleton Coffrin
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


from collections import namedtuple
from heapq import heappush, heappop
from random import shuffle, uniform
from copy import deepcopy

Set = namedtuple("Set", ['index', 'cost', 'items'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    parts = lines[0].split()
    item_count = int(parts[0])
    set_count = int(parts[1])
    
    sets = []
    for i in range(1, set_count+1):
        parts = lines[i].split()
        sets.append(Set(i-1, float(parts[0]), map(int, parts[1:])))
        
    best_solution = [0]*set_count
    sets_list = [i for i in range(set_count)]
    best_obj = 1000000000.0
    
    for niter in range(25):
        coverted = set()
        solution = [0]*set_count
        shuffle(sets_list)
        while True:
            h = []
            for i in sets_list:
                s = sets[i]
                if solution[s.index] == 0:
                    its = []
                    for it in s.items:
                        if it not in coverted:
                            its.append(it)
                    if len(its) > 0:
                        heappush(h, (s.cost * uniform(0.85, 1.15) / len(its), s.index))
            
            if len(h) < 1:
                print('error')
                break
            t = heappop(h)
            #~ print(t)
            solution[t[1]] = 1
            coverted |= set(sets[t[1]].items)
            if len(coverted) >= item_count:
                break
    
        # calculate the cost of the solution
        obj = sum([s.cost*solution[s.index] for s in sets])
        if obj < best_obj:
            best_obj = obj
            best_solution = deepcopy(solution)

    # prepare the solution in the specified output format
    output_data = str(best_obj) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, best_solution))
    

    return output_data


if __name__ == '__main__':
    files_location = ['sc_157_0', 'sc_330_0', 'sc_1000_11', 'sc_5000_1', 'sc_10000_5', 'sc_10000_2']
    i_file = 6
    with open('./data/' + files_location[i_file - 1], 'r') as input_data_file:
        input_data = input_data_file.read()
    print(solve_it(input_data))

#~ import sys

#~ if __name__ == '__main__':
    #~ import sys
    #~ if len(sys.argv) > 1:
        #~ file_location = sys.argv[1].strip()
        #~ with open(file_location, 'r') as input_data_file:
            #~ input_data = input_data_file.read()
        #~ print(solve_it(input_data))
    #~ else:
        #~ print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/sc_6_1)')

