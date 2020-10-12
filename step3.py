import csv        
import pandas as pd
data1 = pd.read_csv('F:/counting1.csv')


print(data1.dtypes)



rows = open('F:/pair.csv')
csv_reader = csv.reader(rows, delimiter=',')
count = 0
year0_5 = {}
for row in csv_reader:
    if count % 2 == 0:
        dict1 = {}
        for n in range(1 , len(row)):
            
            for year in range(1900,2010,10):
                if data1['new_age'][int(row[n])] >= year and data1['new_age'][int(row[n])] < year + 10:
                    if year in dict1:
                        dict1[year] += 1
                    else:
                        dict1[year] = 1
            if data1['new_age'][int(row[n])] >= 2010:
                if 2010 in dict1:
                    dict1[2010] += 1
                else:
                    dict1[2010] = 1
        
        year0_5[int(row[0])] = dict1
        
        if int(row[0]) % 1000 == 0:
            print(row[0])
                
            
    count += 1

print(len(year0_5))   
s = "(r < 1)"
for y in range(1900,2011,10):
    collection = []
    s = str(y) + s
    for z in range(len(data1)):
        if z in year0_5:
            if y in year0_5[z]:
                collection += [year0_5[z][y]]
            else:
                collection += [0]
        else:
            collection += [0]
            
    data1[s] = collection
    
    s = "(r < 1)"
    
    
    
data1.to_csv(r'F:/counting2.csv', index = False, header=True)
