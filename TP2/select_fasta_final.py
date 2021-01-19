#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:24:33 2021

@author: fabre
"""
import argparse

DESCRIPTION = '''This program require a fasta file in entry and a identifiers list,
the program return id associated sequences in an output fasta file
example :  python ~/select_fasta_final -i ~/some_seq_from_ensembl.fa
-seq ENST00000469733,ENST00000414253 -o ~/fasta_outfile.fasta'''

def search_id(input_file, ids_list, outputfile):
    '''  The function returns a dictionary containing the identifiers in key
    and the sequences in value.
    @param inputfile : fasta file path
    @param id_list : search fasta ids
    @param outputfile : path to the new created output file'''
    #initialize variables, the dictionnary will contain only identifiers and sequences request
    dico_fasta = {}
    seq_id = ""
    seq = ""
    #keep_fasta variable check if the dico identifier is in the list
    #(TRUE) of the request identifiers
    keep_fasta = True
    for line in input_file:
        #if the line is not empty
        if not line.startswith('\n'):
        #if line start with "">""
            if line.startswith(">"):
            #if line[0]==">" :
                seq_id = line[1:-1]
                #print (seq_id)
            #if seq_id is in the list containing request id
            #keep_fasta variable remain True else it changes to False
                if seq_id in ids_list:
                    keep_fasta = True
                else:
                    keep_fasta = False
            #if the line doesn't strat with ">"
            else:
                #if keep_fasta variable is true
                #add the sequence to the dictionnary
                if keep_fasta:
                    seq = line[0:-1]
                    dico_fasta[seq_id] = seq
    for keys in dico_fasta:
        #the output file is a fasta file : >identifiers \n sequence (+ \n to separate sequences)
        outputfile.write(">" + keys +"\n" +  dico_fasta[keys] +"\n\n")
    input_file.close()
    outputfile.close()
    #return dico_fasta


def create_parser():
    """This function create new arguments required to run id_search function"""
    parser = argparse.ArgumentParser(add_help=True,
                                     description=DESCRIPTION)

    parser.add_argument('-i', '--input_file',
                        help="Enter the file path",
                        default=None,
                        type=argparse.FileType("r"),
                        metavar="FASTA",
                        required=True)

    parser.add_argument('-seq', '--id_sequences',
                        help="Enter sequence identifiers",
                        type=str,
                        required=True)

    parser.add_argument('-o', '--outputfile',
                        help="Output file",
                        type=argparse.FileType('w'),
                        metavar="FASTA",
                        required=True)
    return parser


def main():
    """
    The main function execute the different previous functions.
    """
    parser = create_parser()
    args = parser.parse_args()
    #define comma as the seperator between sequence identifiers in the list
    search_id(args.inputFile, args.id_sequences.split(","), args.outputfile)


if __name__ == "__main__":
    main()
