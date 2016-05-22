import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Reindex1(olddata):
    lst1 = []
    lst2 = []
    for elem1 in olddata['Year']:
        lst1.append(elem1)
    for elem2 in olddata['Population']:
        lst2.append(elem2)
    olddata = dict([('Year', lst1), ('Population', lst2)])
    newdata = pd.DataFrame(olddata, columns=['Year', 'Population'])
    return newdata

def NewIndexPop(strold):  # add new columns
    lst1 = []
    lst2 = []
    elem1 = strold['Population'].iloc[0]
    for elem2 in strold['Population']:
        lst1.append(elem2 / elem1)
        lst2.append(elem2 - elem1)
        elem1 = elem2
    lst1[0] = np.nan
    lst2[0] = np.nan
    strold['Growth'] = lst2
    strold['%'] = lst1

def Graphs(graph1, var):
    fig = plt.figure()
    if var == 1:
        varstr = 'Growth'
    else:
        varstr = '%'
    lst1 = []
    lst2 = []
    lst3 = []
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)
    for elem in graph1['Year']:
        lst1.append(elem)
    for elem in graph1['Population']:
        lst2.append(elem)
    for elem in graph1[varstr]:
        lst3.append(elem)
    ax1.bar(lst1, lst2, color='green')
    ax2.errorbar(lst1, lst3)
    plt.show()

xls = pd.ExcelFile('growth.xls')
xls = xls.parse('Sheet1')
df = pd.DataFrame(xls)
str1 = df.sort_index(by='Year', ascending=True)  # sort index

str1 = Reindex1(str1)
strdel = Reindex1(str1)
indexstr = 0
for elem in str1['Year']:  # delete elements < 1953
    if elem < 1953:
        strdel = strdel.drop(indexstr, axis=0)
    indexstr += 1

NewIndexPop(strdel)
print(strdel)
var = 1
Graphs(strdel, var)
