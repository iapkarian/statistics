import pandas as pd

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

index = 0
srt2 = pd.DataFrame()
xls = pd.ExcelFile('growth.xls')
xls = xls.parse('Sheet1')
df = pd.DataFrame(xls)
str1 = df.sort_index(by='Year', ascending=True)

str = Reindex1(str1)
for elem in str['Year']:
    if elem < 1955:
        srt2 = str.drop(index, axis=0)
    index += index


print(str)
# df['new'] = #add to end
