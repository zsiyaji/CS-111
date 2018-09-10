#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
"""
Created on Wed Sep 20 16:04:50 2017

@author: Zakariah


def orf_advisor(dna):
    #dna = "CTCATGGACCTCCATTTC"
    print(dna[-3:])
    if dna[0:3] != "ATG":
        return "The first three bases are not ATG"

    elif not (dna[-3:] == "TGA" or dna[-3:] == "TAG" or dna[-3:] == "TAA"):
        return "The last three bases are not a stop codon."

    elif len(dna)%3 != 0:
        return "The string is not of the correct length."

    else:
        return "This is an ORF."

def codon_finder(mrna):
    mrna = "UGUAUAAGGCCGAGG"
    mrna2 = mrna[::-1]
    #make an empty srtring list with length/3 items
    my_list = ["" for x in (range(len(mrna2)//3))]
    count = 0
    for i in range(0,len(mrna2),3):
        my_list[count] = mrna2[i:i+3]
        count += 1
    my_list[0] = ("AUG")
    my_list.append("UAG")
    print( "The codons", my_list, "make a protein that is MAGIC")
"""
def findX(x,y):
    return x,y

print(findX(2,3))
