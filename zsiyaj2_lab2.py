# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
"""
#Lab 2
#Author: Zakariah Siyaji
#Date: September 7th, 2017

A = 400
C = 323
G = 20202
T = 212
totalCount = A+G+C+T
print("The total length of the DNA string is:",totalCount)
def get_codon(str):
    print(str[0:3])
str1 = input("Enter The DNA and I will output your first codon: ")
get_codon(str1)
"""

#x = int(input("Enter an integer: "))
#y = int(input("Enter another integer: "))
#z = int(input("Enter your final integer: "))

#sums = x+y+z
#print("The sum of: ", x , " and " ,y , " and " ,z, " is " , sums, sep='')






Man = {'Homo' : ['erectus', 'neanderthalensis', 'sapiens', 'habilis']}



if 'erectus' in Man == True:
    print(True)
else:
    print(False)
