#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 15:23:44 2017

@author: Zakariah Siyaji
Lab 5 for CS111 for Professor Sloan and Poretsky
"""


def comp_nuc(first,second):
    '''
    If we were to indentify whether or not the second
    parameter was either a DNA or mRNA strand, then
    the following code inside of the docstrings would
    have identified such an issue:

    def nucleo():
        for i in len(second):
            count = 0
            if (second[i] == "T"):
                count = count + 1
                if count > 1:
                    return True
                else:
                    return False
    '''
    if (second == "DNA"):
        if first == "A":
            return "T"
        elif first == "T":
            return "A"
        elif first == "C":
            return "G"
        else:
            return "C"
    else:
        if first == "A":
            return "U"
        elif first == "U":
            return "A"
        elif first == "C":
            return "G"
        else:
            return "C"

def comp_to_dna(first):
    first1 = ""
    first1 = first[::-1]
    first2 = ""
    for i in range(0, len(first)):
       if first1[i] == "A":
           first2 = first2 + "T"
       elif first1[i] == "T":
           first2 = first2 + "A"
       elif first1[i] == "C":
           first2 = first2 + "G"
       else:
           first2 = first2 + "C"

    return first2

def comp_to_rna(first):
    first1 = ""
    first1 = first[::-1]
    first2 = ""
    for i in range(0, len(first)):
       if first1[i] == "A":
           first2 = first2 + "U"
       elif first1[i] == "U":
           first2 = first2 + "A"
       elif first1[i] == "C":
           first2 = first2 + "G"
       else:
           first2 = first2 + "C"

    return first2

def gc_content(first):
    count = 0
    count1 = 0
    for i in range (0,len(first)):

        if (first[i] == "G"):
            count = count + 1
        if (first[i] == "C"):
            count1 = count1 + 1

#    final = ((count + count1) / len(first))
    """
    To create the fraction, I followed the directions on Piazza given by the
    instructors. It was slightly difficult to undertand. But, you can also see that
    I created a variable by the name of "final" which would then return a float value.
    """
    return "The count of G's are", count, "and the count of C's are", count1,". ", "The fraction of G+C in the total DNA strand =", (count + count1), "/", (len(first))

def main():
    comp_nuc('A','DNA')
