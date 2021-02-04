#!/usr/bin/python
# _*_ coding: utf-8 _*_
import os
import sys

def save_result(filename, results):
    with open(filename, "a") as f:
    	for line in results:  
        	f.write(line) 

def parse_file(filename, keyword):
	found_lines = []
	with open(filename) as f:
		for line in f.readlines():
			idx = line.find(keyword)
			if idx != -1:
				found_lines.append(line[idx:])
	

	print '%s, total found: %d' % (filename, len(found_lines))
	return found_lines


g = os.walk('./')  
total_found_lines = []

keyword = sys.argv[1]
save_file = sys.argv[2]

for path, dir_list, file_list in g:  
    for file_name in file_list:
    	if file_name.find('.log') != -1:
	    	filename = os.path.join(path, file_name)
	    	found = parse_file(filename, keyword)
	    	total_found_lines.append('------ Found In %s (%d) ------\n' % (filename, len(found)))
	    	total_found_lines.extend(found)

save_result(save_file, total_found_lines)
