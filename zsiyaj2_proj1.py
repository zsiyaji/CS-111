"""
Zakariah Siyaji
Project 1 for Professor Sloan and Poretsky
Written on Wednesday October 18th, 2017
We worked on this project with Lola and Daisy at the CS Lounge
on October 19th, and 20th.
"""
def get_orf(DNA):
    codon = ""
    if DNA[0:3] == "ATG":
        k = 0
        j = 3
        for i in range (0, len(DNA)):
            codon = codon + DNA[k:j]
            #print(DNA[k:j])
            #print(DNA[k+3:j+3])
            #print(codon)
            if DNA[(k+3):(j+3)] in ["TAG", "TAA", "TGA"]:
            #if DNA[(k):(j)] in ["TAG", "TAA", "TGA"]:
                return codon
            if ((j+3)==(len(DNA)+1)) or ((j+3)==(len(DNA)+2)) or ((j+3)==(len(DNA)+3)):
                return DNA
            k += 3
            j += 3

def one_frame(DNA):
    flag = True
    newList = []
    i = 0
    while i<len(DNA):
        #while i != len(DNA):
        #print(i)
        if DNA[i:i+3] == "ATG":
            str1 = get_orf(DNA[i:])
            newList.append(str1)
            i += len(str1)
        #print(DNA[i:i+3])
        #print(str1)
        i += 3
    return newList

def find_all_orfs(DNA):
    newList1 = one_frame(DNA[0:])
    newList2 = one_frame(DNA[1:])
    newList3 = one_frame(DNA[2:])
    return newList1 + newList2 + newList3

def gc_content(str1):
    length = len(str1)
    Gcount = 0
    Ccount = 0
    for i in range(length):
        if str1[i] == 'C' :
            Ccount += 1
        elif str1[i] == 'G':
            Gcount += 1
        else:
            continue
    GC = round(float(Gcount + Ccount )*100/length,2)
    return GC

def gene_finder(file_name, min_len, min_GC):
    file = open(file_name)
    DNA = file.read()
    allorfs = find_all_orfs(DNA)
    newList = []
    for i in allorfs:
        length = len(i)
        GC = gc_content(i)
        if( length > min_len and GC > min_GC):
            newList.append([i,length, GC])
    return newList

result = gene_finder("X73525.fasta", 1, 10)
for i in range(len(result)):
	print('{} : {} ' .format(i,result[i]))

#
#
#print("TESTS: -------------------------------------")
#print("Testing one_frame")
#print(one_frame("AATGCCATGTGAATGCCCTAA"))
#print("Answer: ['ATG', 'ATGCCC']")
#print(one_frame("ATGCCCATGGGGAAATTTTGACCC"))
#print("Answer: ['ATGCCCATGGGGAAATTT']")
#print("TESTS: -------------------------------------")
#print("Testing find_all_orfs")
#print(find_all_orfs("ATGGGATGAATTAACCATGCCCTAA"))
#print("Answer: ['ATGGGA', 'ATGCCC', 'ATGAAT']")
#print(find_all_orfs("GGAGTAAGGGGG"))
#print("Answer: []")
#print("TESTS: -------------------------------------")
