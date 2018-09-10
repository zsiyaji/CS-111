from child2parent_dict import tax_dict
from yeast_dict import yeast_dict

def list_ancestors(taxon, dict1):
    lst = []
    lst.append(taxon)
    while True:
        if taxon in dict1.keys():
            lst.append(dict1[taxon])
            taxon = dict1[taxon]
            continue
        else:
            return lst

def root(dict1):
    taxon = list(dict1.keys())[0]
    lst = list_ancestors(taxon,dict1)
    return lst[-1]

def kids(taxon,dict1):
    lst =[]
    if taxon in dict1.values():
        for kid,parent in dict1.items():
            if taxon == parent:
                lst.append(kid)
    return lst
def common_ancestor(taxlist,dict1):
    if len(taxlist) == 0:
        return []
    else:
        ancestorList = []
        for taxon in taxlist:
            ancestorList.append(list_ancestors(taxon,dict1))
    list0 = ancestorList[0]
    for taxon in list0:
        counter = 0
        for i in range(1,len(ancestorList)):
            if taxon in ancestorList[i]:
                counter += 1
        if counter == len(ancestorList) -1:
            return taxon
        else:
            continue
def c_ancestor(taxlist,dict1):
    newdict = dict()
    for key,value in dict1.items():
        if ord(key[0]) >= 65 and ord(key[0]) <= 91 and key.count(' ') == 1:
            list1 = key.split(' ')
            key = key[0] + ". " + list1[1]
            newdict[key] = value
    if len(taxlist) == 0:
        return []
    else:
        ancestorList = []
        for taxon in taxlist:
            ancestorList.append(list_ancestors(taxon,newdict))
    list0 = ancestorList[0]
    for taxon in list0:
        counter = 0
        for i in range(1,len(ancestorList)):
            if taxon in ancestorList[i]:
                counter += 1
        if counter == len(ancestorList) -1:
            return taxon
        else:
            continue
print(list_ancestors('Pan troglodytes', tax_dict))
print(common_ancestor(['Hominoidea','Pan troglodytes'],tax_dict))
print(common_ancestor(['Hominoidea','Pan troglodytes','Lorisiformes'],tax_dict))
print(common_ancestor(['Hominoidea','Pongo abelii'],tax_dict))
print(c_ancestor(['Hominoidea','P. abelii'],tax_dict))
print(root(tax_dict))
print(kids('Primates',tax_dict))
