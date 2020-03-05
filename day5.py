#!/usr/bin/env python3

import os
import argparse
import glob

parser = argparse.ArgumentParser()
parser.add_argument("--path", help="Specified director", required=True)
parser.add_argument("--version", action="version", help="Number of version", version='v1.0 by Anastasiya Brytsikava')
parser.add_argument("--file_per_dir", action="store_true", help="Outputs files only from the parent directory")
parser.add_argument("--list_file_rec", action="store_true", help="List files recursive")
parser.add_argument("--extension", help="Filter by file extension")
parser.add_argument("--output_filename", action="store_true", help="Order output by filename")
parser.add_argument("--output_data", action="store_true", help="Order output by data of creation")
args = parser.parse_args()

def rec(path):
    for root,dirs,files in os.walk(path):
        for i in files:
            print(os.path.join(root,i))

def list_files_ext(spis,extension):
    print('Files with extension:')
    for file in spis:
        if file.endswith('.' + extension):
            print(os.path.abspath(file))


def data_time(spis):
        time_sorted_list = sorted(spis, key = os.path.getmtime)
        return(time_sorted_list)

def func():
    
    if not args.file_per_dir:
        tmp = [os.path.join(args.path, f) for f in os.listdir(args.path)]

    if args.file_per_dir:
        parent = os.path.abspath(os.path.join(args.path, '..'))
        tmp = [os.path.join(parent, f) for f in os.listdir(parent) if os.path.isfile(os.path.join(parent, f))]


    if args.list_file_rec:
        print('List files recursive:')
        print(rec(args.path))
 

    if args.output_data:
            tmp = data_time(tmp)


    if args.output_filename:
            tmp = sorted(f for f in tmp if os.path.isfile(os.path.join(args.path, f)))

    if args.extension:
            tmp = list_files_ext(tmp, args.extension)

    if type(tmp) == list:
        print('\n'.join(tmp))
    else:
        print(tmp)
 
func()

