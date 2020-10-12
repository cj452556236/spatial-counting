import csv        
import pandas as pd
data1 = pd.read_csv('F:/counting3.csv')


print(data1.dtypes)




rows = open('F:/pair2.csv')
csv_reader = csv.reader(rows, delimiter=',')
count = 0
year0_5 = {}

for row in csv_reader:
    if count % 2 == 0:
       year0_5[int(row[0])] = [len(row) - 1] 
        
                
            
    count += 1

print(len(year0_5))  

s = "(r < 0.5)"
collection = []
for z in range(len(data1)):
    if z in year0_5:
        collection += [year0_5[z]]
    else:
        collection += [0]
data1[s] = collection
        
    

    
    
    
data1.to_csv(r'F:/counting4.csv', index = False, header=True)
