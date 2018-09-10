# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 21:00:26 2017

@author: Zakariah Siyaji
For Professor Sloan and Poretsky
Lab 9

Help on this lab was provided by:
Dr. Sanjay Kumar of IIT, India

"""




#Accesion number: GQ366752
#FASTA (DNA STRAND): "TTAGCGCCGGAGCCGGCGGTAGTGTTCAATGCACTGGCGTCCAGCAGGTAGCTGTAAGTAGTTCAAGACTGTGTATGGCCATCTGCAGCCCACAGTTTTTAGCTTCTCCAAAATGACCATATTCTGTCCACATTCTTTATCCCTTTCTATCTATAAGCCTACCACACTCCAGACTCACCCAGTCAGCAGTGCAA"


aminoDict = {}
def codonToAminoAcid():
    global aminoDict
    finalList = []
    with open("gencode",'r') as f:
        _header = True
        for line in f:
            if _header == True:
                _header = False
                continue
            line = line.replace('}','')
            line = line.replace('\'','')
            line = line.replace(' ','')
            line = line.strip()
            temp = line.split(',')[:-1]
            finalList.extend(temp)
    f.close()

    for item in finalList:
        key,value = item.split(':')
        aminoDict[key] = value

def reverse(string):
    newstring = ''
    for i in range(len(string)-1,-1,-1):
        newstring += string[i]
    return newstring

def translate_reverse(DNA):
    DNA = DNA.upper()
    # doing reverse string
    DNA = reverse(DNA)

    #translating the DNA with string methods

    trans = str.maketrans('ACGT','TGCA')
    DNA = DNA.translate(trans)

    return translate_dna(DNA)

def translate_dna(DNA):
    DNA = DNA.upper()
    if DNA.find("ATG") >= 0:
        loc = DNA.find("ATG")
        splitDNA = []
        for i in range(loc,len(DNA),3):
            if i + 3 <= len(DNA):
                splitDNA.append(DNA[i:i+3])
        #now we have the value of splitDNA set
        protein = ""
        for item in splitDNA:
            if item in aminoDict:
                protein += aminoDict[item]
            else:
                protein += 'X'

    else:
        splitDNA = []
        for i in range(0,len(DNA),3):
            if i + 3 <= len(DNA):
                splitDNA.append(DNA[i:i+3])
        protein = ""
        for item in splitDNA:
            if item in aminoDict:
                protein += aminoDict[item]
            else:
                protein += 'X'
    return protein

codonToAminoAcid()
print(translate_dna("TTAGCGCCGGAGCCGGCGGTAGTGTTCAATGCACTGGCGTCCAGCAGGTAGCTGTAAGTAGTTCAAGACTGTGTATGGCCATCTGCAGCCCACAGTTTTTAGCTTCTCCAAAATGACCATATTCTGTCCACATTCTTTATCCCTTTCTATCTATAAGCCTACCACACTCCAGACTCACCCAGTCAGCAGTGCAA"))
#print(translate_dna("CCAATGATCGATCGATCGTTGCTTATCGATCAG"))
#print(translate_dna("atgactgatcgtagcttgcttacgtatcgtat"))
#print(translate_dna("CGAATGACGATCGATCGTNACGTACGATCGTACTCG"))
print(translate_reverse("GAATTC"))
print(translate_reverse("AATTCCGGCATG"))
