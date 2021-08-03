#!/usr/bin/env python3
import hashlib
import argparse
import os

def main():
    conf_file_name, directory = process_args()
    if conf_file_name and directory:
        file_list = load_conf_file(conf_file_name)        
        if file_list:
            check_files(file_list, directory)

def process_args():
    parser = argparse.ArgumentParser(
        description="Read input file and check integrity of files listed there.\
            The arguments are mandatory.")
    parser.add_argument('input_file', metavar='<input_file>', type=str, 
                        help='path to the input file') 
    parser.add_argument('directory', metavar='<directory>', type=str, 
                        help='path to the directory containing the files to check') 
    args = parser.parse_args()
    return args.input_file, args.directory

def load_conf_file(file_name):
    file_list = []
    try:
        with open(file_name) as fh:
            for lino, line in enumerate(fh.readlines()):
                pars = line.strip().split(' ')
                if (len(pars) == 3 and pars[1].lower() in ('md5', 'sha1', 'sha256')):
                    file_list.append(pars)
                else:
                    print("Error interpreting {} line No {}, skipping\n".format(
                        os.path.basename(file_name), lino+1))
    except EnvironmentError as err:
        print("Error loading input file{}\n\n{}".format(
            os.path.basename(file_name), err))
    return file_list        

def check_files(file_list, folder):    
    for file in file_list:
        file_name, alg, hash = file
        module = eval('hashlib.'+alg.lower()+'()')
        try:            
            with open(os.path.join(folder, file_name), 'rb') as fh:
                module.update(fh.read())
        except EnvironmentError as err:            
            print_result(os.path.basename(file_name), "NOT FOUND")
            continue
        if module.hexdigest() == hash:
            print_result(os.path.basename(file_name), "OK")
        else:
            print_result(os.path.basename(file_name), "FAIL") 

def print_result(file_name, res):
    WIDTH = 15
    print("{file_name:<{WIDTH}} {res}".format(**locals()))

if __name__ == '__main__':
    main()
