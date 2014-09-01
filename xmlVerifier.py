# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 13:42:42 2014

@author: ankur
"""

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from glob import glob
import sys,os

def parsefile(file):
    parser = make_parser()
    parser.setContentHandler(ContentHandler())
    parser.parse(file)

def check_xml(filename):
    try:
        parsefile(filename)
        print "%s is well-formed" % filename
    except Exception, e:
        f = open("log","a")
        print "%s is NOT well-formed! %s" % (filename, e)
        f.write(filename)
        f.close()
            
            
def readFiles():
    
    total_files = [f for f in os.listdir('./check')]
    for i in total_files:
        
            filename ="./check/" + i
            fo = open(filename, "r")
            lines = fo.readlines()
            fo.close()
            to_read = len(lines)-10
            line1 = lines[:to_read]
            line2 = lines[to_read+2:]
            line = line1+ line2
            new_file = "./new/" +i
            with open(new_file, 'w') as f:
                f.writelines(line)
            #check_xml(new_file)
                   
readFiles()
