#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''This code takes as input a gtf type file and return the length for each transcripts'''
import re

transcript_start = dict()
transcript_end = dict()

def get_genomic_length(input_file=None):
    ''' This function record the smallest value for each transcript in
    the transcript_start dictionary, and the highest value in the
    transcript_end dictionary. the subtraction of the 2 values
    gives the length for each transcript'''
    file_handler = open(input_file)
    for line in file_handler:
        token = line.split("\t") #split by tabs
        start = int(token[3]) #start of current element
        end = int(token[4]) #end of current element

        tx_id = re.search('transcript_id "([^"]+)"', token[8]).group(1) #transcript identifier

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
