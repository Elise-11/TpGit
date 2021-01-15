#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''This code takes as input a gtf type file and return the length for each transcripts '''
import re

transcript_start = dict()
transcript_end = dict()

def get_genomic_length(input_file=None):
    ''' This function record the smallest value for each transcript in the dictionary named transcript_start,
    and the highest value in the dictionary named transcript_end. the subtraction of the 2 values ​​
    gives the length for each transcript'''
    file_handler = open(input_file)
    for line in file_handler:
        token = line.split("\t")
        start = int(token[3])  # le début de l'élément courant
        end = int(token[4])  # la fin de l'élément courant
        # L'identifiant du transcrit

        tx_id = re.search('transcript_id "([^"]+)"', token[8]).group(1)

        if tx_id not in transcript_start:

            transcript_start[tx_id] = start
            transcript_end[tx_id] = end

        else:

            if start < transcript_start[tx_id]:

                transcript_start[tx_id] = start

                if end > transcript_end[tx_id]:
                    transcript_end[tx_id] = end

    for tx_id in transcript_start:
        print(tx_id + "\t" + str(transcript_end[tx_id] - transcript_start[tx_id] + 1))


if __name__ == '__main__':
    get_genomic_length(input_file='../pymetacline/data/gtf/simple.gtf')
