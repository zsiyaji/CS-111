"""

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
            print(len(DNA))
            print(k+3)
            print(j+3)
            if DNA[(k+3):(j+3)] in ["TAG", "TAA", "TGA"]:
                return codon
            if ((j+3)==(len(DNA)+1)) or ((j+3)==(len(DNA)+2)):
                return DNA
            k += 3
            j += 3


def read_seq(Filename, num):
    x = [0] * num
    lines = open(Filename).read().split("\n")
    j = 0
    for i in range(0, len(lines)-1):
        if lines[i][0] == ">":
            y = lines[i+1]
            x[j] = len(y)
            print(lines[i+1])
            print("\n\n")
            j += 1
    return x

print(get_orf("ATGTGAA"))
print(get_orf("ATGAGATAGG"))
print(get_orf("ATGAGATAGGGGTAA"))
print(get_orf("ATGAAATT"))
#print(read_seq("atp_synthase(2) (1).faa",4))
