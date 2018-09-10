#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:31:18 2017

@author: Zakariah Siyaji
Date: September 12th, 2017
Lab Assignment 3, Dr. Sloan CS 111 Green
"""




dna_sequence = input("Enter your gene: ")
def get_info(dna_sequence):
    count = 1
    count_a = 0
    count_c = 0
    count_t = 0
    count_g = 0 
    
   # newCounter = 0
    while count < len(dna_sequence):
        count += 1
    for i in range(len(dna_sequence)):
        
        if dna_sequence[i] == "A":
            count_a += 1
        elif dna_sequence[i] == "C":
            count_c += 1
        elif dna_sequence[i] == "G":
            count_g += 1 
        elif dna_sequence[i] == "T":
            count_t += 1
    total_base_pairs = count_a + count_g + count_c + count_t
    print("The total length of the gene is:", count, "bases")  
    print("There are",count_a ,"A’s")
    print("There are",count_c ,"C’s")
    print("There are",count_g ,"G’s")
    print("There are",count_t ,"T’s")
    print("Percent of A =",(count_a/total_base_pairs)*100,"%")
    print("Percent of C =",(count_c/total_base_pairs)*100,"%")
    print("Percent of G =",(count_g/total_base_pairs)*100,"%")
    print("Percent of T =",(count_t/total_base_pairs)*100,"%")
    #print("The number of amino acids are: ", newCounter)  
    
    counter = len(dna_sequence)//3    
    print("The amount of amino acids are approximately (+/-)" , counter) 
get_info(dna_sequence)


n=int(input("n="))
P=[]

for i in range (2,int(n**1/2)):
    if(n % i == 0):
        P.append(i)
        n = n/i
print(P)


"""
Streptococcus pneumoniae strain CCARM 4084 RNA polymerase alpha subunit (rpoA) gene, partial cds
Accession: GU045413

GTTCGTGAAGACGTGATGCAAATCATTCTGAACATTAAGGGAATTGCAGTGAAATCGTACGTTGAAGACG
AAAAAATCATCGAACTGGATGTTGAAGGTCCTGCTGAAGTAACAGCTGGTGACATTTTGACAGATAGCGA
TATTGAAATTGTAAATCCAGATCATTATCTCTTTACAATCGGTGAAGGTTCTTCTCTAAAAGCGACTATG
ACTGTTAACAGTGGTCGTGGATATGTACCTGCTGACGAAAATAAAAAGGATAATGCACCAGTTGGAACAC
TTGCTGTAGATTCTATTTATACACCAGTTACAAAAGTCAACTATCAAGTGGAACCTGCTCGTGTAGGTAG
CAATGATGGTTTCGACAAATTAACCCTTGAAATCTTGACAAATGGAACAATTATTCCAGAAGATGCTTTA
G

Pneumococcal disease is an infection caused by Streptococcus pneumoniae bacteria.  
These bacteria can cause many types of illnesses, including: pneumonia (infection of the lungs), 
ear infections, sinus infections, meningitis (infection of the covering around the brain and spinal cord), 
and bacteremia (blood stream infection). Pneumococcus bacteria are spread through coughing, sneezing, 
and close contact with an infected person.
"""