#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This program is a parser, from a fasta file the user passes an arg seq,
the program return associated sequences. """

import argparse
from Bio import SeqIO

def create_parser():
    """This function create arguments required to run later the id search."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputfile', type=str, metavar="FASTA", required=True)
    parser.add_argument('-id_seq', '--id_sequences', type=str, required=True)
    return parser

def search_id(inputfile=None, id_sequences=None):
    """This function uses SeqIo from Biopython
    it searchs differents id required by the user
    and return the associated sequence."""
    handle = open(inputfile, "r")
    print("Processing fasta file ...\n")

    for record in SeqIO.parse(handle, "fasta"):
        if record.id in id_sequences:
            seq_id = record.id
            seq = str(record.seq)
            print(">" + seq_id + "\n" + seq + "\n")
    print("here are the requested sequences!")
    handle.close()

def main():
    """This main function execute the to previous functions."""
    parser = create_parser()
    args = parser.parse_args()
    args = args.__dict__
    print(args['inputfile'])
    search_id(args["inputfile"], args["id_sequences"])

if __name__ == "__main__":
    main()
