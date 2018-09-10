#!/usr/bin/python
#CS 111 Green - Program Design 1
#Tutor: Sanjay Kumar, Chegg Tutor and PhD Student at IIT, India.
#Professors: Sloan & Poretsky
#Student: Zakariah Siyaji


import csv
import matplotlib.pyplot as plt
def plotdata(csvFile,col1,col2):
    dict1 = {}
    with open(csvFile,'rb') as f:
        data = csv.reader(f)
        for line in data:
            if len(line) < 4:
                break
            if line[4] not in dict1:
                dict1[line[4]] = {}
                dict1[line[4]]['x'] = [line[col1]]
                dict1[line[4]]['y'] = [line[col2]]
            else:
                dict1[line[4]]['x'].append(line[col1])
                dict1[line[4]]['y'].append(line[col2])
    f.close()
    print(dict1)
    #plt.scatter(xList,yList)
    #plt.show()
    for family,valueList in dict1.items():
        if family == "Iris-setosa":
            plt.scatter(valueList['x'],valueList['y'],color='r',label='Iris-setosa')
        elif family == "Iris-versicolor":
            plt.scatter(valueList['x'],valueList['y'],color='b',label='Iris-versicolor')
        elif family == "Iris-virginica":
            plt.scatter(valueList['x'],valueList['y'],color='g',label='Iris-virginica')
    plt.xlabel('Sepal Length Cm')
    plt.ylabel('Sepal Width Cm')
    plt.title("Sepal Width Vs. Sepal Length")
    plt.legend(loc='best')
    plt.show()
plotdata('iris.csv',0,2)
