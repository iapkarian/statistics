import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter.tix


def main_window(w, df):
    w.title('Population growth')
    tab = tkinter.tix.HList(w, columns=4, header=True, width=30, height=35)
    tab.grid(row=0, column=0, columnspan=3, )
    tab.header_create(0, text="Year")
    tab.header_create(1, text="Population")
    tab.header_create(2, text="Growth")
    tab.header_create(3, text="%")

    index = 0
    for elem in df['Year']:
        tab.add(index, data="--<%s>--" % index)
        tab.item_create(index, 0, text=str(elem))
        index += 1

    index = 0
    for elem in df['Population']:
        tab.item_create(index, 1, text=str(elem))
        tab.item_create(index, 2, text=str(elem))
        tab.item_create(index, 3, text=str(elem))
        index += 1

def reindex1(olddata):
    lst1 = []
    lst2 = []
    for elem1 in olddata['Year']:
        lst1.append(elem1)
    for elem2 in olddata['Population']:
        lst2.append(elem2)
    # olddata = dict([('Year', lst1), ('Population', lst2)])
    olddata = {'Year': lst1, 'Population': lst2}
    newdata = pd.DataFrame(olddata, columns=['Year', 'Population'])
    return newdata


def new_index_pop(strold):  # add new columns
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


def graphs(graph1):
    print('fff')
    fig = plt.figure()
    lst1 = []
    lst2 = []
    lst3 = []
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)
    for elem in graph1['Year']:
        lst1.append(elem)
    for elem in graph1['Population']:
        lst2.append(elem)
    for elem in graph1['Growth']:
        lst3.append(elem)
    ax1.bar(lst1, lst2, color='green')
    ax2.errorbar(lst1, lst3)
    plt.show()

xls = pd.ExcelFile('growth.xls')
xls = xls.parse('Sheet1')
df = pd.DataFrame(xls)
str1 = df.sort_index(by='Year', ascending=True)  # sort index

str1 = reindex1(str1)
strdel = reindex1(str1)
indexstr = 0
for elem in str1['Year']:  # delete elements < 1953
    if elem < 1953:
        strdel = strdel.drop(indexstr, axis=0)
    indexstr += 1

new_index_pop(strdel)

root = tkinter.tix.Tk()
main_window(root, strdel)

graphs(strdel)
root.mainloop()
