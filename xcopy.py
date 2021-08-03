#!/usr/bin/env python3
import os
import argparse
import shutil
import xml
import xml.etree.ElementTree as ET

def main():    
    conf_file_path = process_parameters()
    file_list = parse_conf_file(conf_file_path)
    if file_list:
        do_copy(file_list)

def process_parameters():
    parser = argparse.ArgumentParser(
        description="Copy files according to the provided configuration file.")
    parser.add_argument('conf_file', metavar='<conf_file>', type=str, 
                        help='path to the input file') 
    args = parser.parse_args()
    return args.conf_file

def parse_conf_file(conf_file):
    file_list = []
    try:
        tree = ET.parse(conf_file)
    except (EnvironmentError, xml.etree.ElementTree.ParseError) as err:
        print("\nError loading configuration file:\n\n{}\n".format(err))        
    else:
        for element in tree.findall('file'):        
            try:
                data = [element.get(attribute) for attribute in ('source_path',
                'destination_path', 'file_name')]
                file_list.append(data)
            except (ValueError, LookupError) as err:
                print('Error interpreting configuration file: {}'.format(err))
        return file_list
    
def do_copy(file_list):
    count = 0
    for file in file_list:
        source = os.path.join(file[0], file[2])
        dest = file[1]
        file_name = file[2]
        try:            
            shutil.copy(source, dest)
            count += 1
            print_result(file_name, None)
        except EnvironmentError as err:
            print_result(file_name, err)
            continue
    print("\n{} of {} files copied\n".format(count, len(file_list)))

def print_result(file_name, err):
    WIDTH = 15
    if err is None:
        print("{file_name:<{WIDTH}} copied".format(**locals()))
    else:
        print("{file_name:<{WIDTH}} failure: {err}".format(**locals()))    

if __name__ == '__main__':
    main()
