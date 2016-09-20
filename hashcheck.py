#!/usr/bin/env python
"""Generates SHA1 or MD5 hash of a given file.
Optionally, takes a hash value as input and compares it to the file's hash.
SHA1 is default hashing algorithm, but MD5 can be specified.
Blocksize 65536 is default, but any other blocksize can be specified
"""
import argparse
import hashlib

# TODO: add a console progress bar
# TODO: add OS check
# TODO: add unit tests

PARSER = argparse.ArgumentParser()
PARSER.add_argument("-i", "--inputfile", required=True,
                    help="input file to check hash on")
PARSER.add_argument("-H", "--hashvalue",
                    help="input hash value, if you want to automatically compare")
PARSER.add_argument("-a", "--algorithm", default="sha1",
                    choices=['sha1', 'md5'], help="input hash algorithm type")
PARSER.add_argument("-b", "--blocksize", default=65536,
                    type=int, help="specify a blocksize")
ARGS = PARSER.parse_args()

print "\nhashvalue given:\t", ARGS.hashvalue
print "algorithm given:\t", ARGS.algorithm
print "blocksize set to:\t", ARGS.blocksize

if ARGS.algorithm == 'sha1':
    HASHER = hashlib.sha1()
elif ARGS.algorithm == 'md5':
    HASHER = hashlib.md5()

print "\nhashing file...\n"
with open(ARGS.inputfile, 'rb') as afile:
    BUF = afile.read(ARGS.blocksize)
    while len(BUF) > 0:
        HASHER.update(BUF)
        BUF = afile.read(ARGS.blocksize)
        HEXDIGEST = HASHER.hexdigest()

print "\n", ARGS.algorithm, " hash of ", ARGS.inputfile, ": ", HEXDIGEST, "\n"

if ARGS.hashvalue:
    if ARGS.hashvalue == HEXDIGEST:
        print "\033[92m", "file\'s hash matches given hash...\n"
    else:
        print "\033[91m", "file\'s hash DOES NOT MATCH given hash\n"
