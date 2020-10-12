import csv        
d1 = {}
d0_5 = {}
rows = open('matrix_final.csv')
csv_reader = csv.reader(rows, delimiter=',')
count = 0
for row in csv_reader:
    for n in range(count,len(row)):
        if float(row[n]) < 0.5:
            if count in d0_5:
                d0_5[count] += [n + 1]
            if count not in d0_5:
                d0_5[count] = [n + 1]
            if n + 1 in d0_5:
                d0_5[n + 1] += [count]
            
               
            if n + 1 not in d0_5:
                d0_5[n + 1] = [count]
            
                
                
        if float(row[n]) < 1:
            if count in d1:
                d1[count] += [n + 1]
            if count not in d1:
                d1[count] = [n + 1]
                
            
               
            if n + 1 in d1:
                d1[n + 1] += [count]
            if n + 1 not in d1:
                d1[n + 1] = [count]
    if count % 1000 == 0:
        print(count)
    count += 1
import collections
od0_5 = collections.OrderedDict(sorted(d0_5.items()))
od1 = collections.OrderedDict(sorted(d1.items()))
f = open('pair.csv', 'w')
writer = csv.writer(f)
    
for k1,v1 in od1.items():
    r1 = [k1] + v1
    writer.writerow(r1)
f.close()

f2 = open('pair2.csv', 'w')
writer2 = csv.writer(f2)
    
for k2,v2 in od0_5.items():
    r2 = [k2] + v2
    writer2.writerow(r2)
f2.close()
