#! /usr/bin/env python
# coding: utf-8

import argparse
import logging as lg    # lg levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
import os
import sys

from glob import glob

def debug(func):    # activate with @debug
    def inner(*args, **kwargs):
        lg.debug('Running method: %s', func.__name__)
        try:
            return func(*args, **kwargs)
        except Exception as e:
            lg.error(e.message)
            lg.error(str(e))
            raise
    return inner

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("selector", help="Files to select in the directory, type: string", default="*")
    parser.add_argument("-v", "--verbose",action='store_true', help="""Activate verbose mode""")
    parser.add_argument("-d", "--debug",action='store_true', help="""Activate debug mode""")
    parser.add_argument("-a", "--append",help="""Append string at the end of the files""")
    parser.add_argument("-i", "--insert",help="""Insert String at the start of the file""")
    parser.add_argument("-l", "--list",action="store_true", help="""List files of selection""")
    parser.add_argument("-re", "--reindex",action="store_true", help="""Reindex all selected files by creation date from 0 to N, n the number of files. The number will be appended at the begining of the file""")
    parser.add_argument("-rm", "--remove",action="store_true", help="""Remove files""")
    return parser.parse_args()

def pad(number,padding):
    ## add as much 0s as needed
    return "0"*(padding - len(str(number))) + str(number)

class Renamer():
    def __init__(self,path="./*"):
        self.path = path
        lg.info("Path has been defined as : %s", path)
        self.folder = os.path.split(path)[0]
        lg.info("Folder has been defined as : %s", self.folder)
        # Save the file listing corresponding to the selection
        self.filename_list = [os.path.split(item)[1] for item in self.select(self.path)]
        lg.info("Filelist : \n %s", self.filename_list )

    ######################### Global Functions

    # Join filename with full folder path in this rename function
    def rename(self,filename, new_filename):
        os.rename(os.path.join(self.folder,filename),os.path.join(self.folder,new_filename))

    def select(self,selection):
        try:
            return sorted(glob(selection))
        except OSError as ose :
            lg.error("Directory does not exist")
            sys.exit()

    ###########################  Action functions 

    def insert(self, text):
        for filename in self.filename_list:
            self.rename(filename,text+filename)
            lg.info("File %s renamed into %s",filename,text+filename)

    def append(self,text):
        for filename in self.filename_list:
            split = filename.rsplit(".",1)
            #Handles the possibility of a namefile with multiple extensions ex: toto.txt.jpg
            if len(split) == 2:
                new_name = split[0] + text +"."+ split[1]
            elif len(split) == 1:
                new_name = split[0] + text
            self.rename(filename,new_name)
            lg.info("File %s renamed into %s",filename,new_name)

    def list(self):
        for filename in self.filename_list:
            print filename

    def remove(self):
        for filename in self.filename_list:
            os.remove(os.path.join(self.folder,filename))
            lg.info("File %s has been removed", filename)

    def reindex(self):
        fileList = sorted(self.select(self.path),key=lambda x: os.stat(x).st_birthtime)
        self.filename_list = [os.path.split(item)[1] for item in fileList]
        lg.info("%i files are gonna be sorted",len(fileList))
        padding = len(str(len(self.filename_list)))
        ind = 0
        for filename in self.filename_list:
            new_name = pad(ind,padding) + "_" + filename
            self.rename(filename, new_name)
            lg.info("File %s renamed into %s",filename,new_name)
            ind +=1

def main():
    # Parse arguments
    args = parse_arguments()
    if args.verbose :
        lg.basicConfig(level=lg.INFO)
    elif args.debug :
        lg.basicConfig(level=lg.DEBUG)

    # Main
    r = Renamer(args.selector)
    if args.list:
        r.list()
    elif args.reindex:
        r.reindex()
    elif args.remove:
        r.remove()
    elif args.insert is not None:
        r.insert(args.insert)
    elif args.append is not None:
        r.append(args.append)


if __name__ == "__main__":
    main()
    lg.info("Exiting program")