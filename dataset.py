from collections import Counter
import csv

with open ("HeightWeight.csv",newline="")as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
heightdata=[]

for i in range(len(filedata)):
    num=filedata[i][1]
    heightdata.append(float(num))

n=len(heightdata)
total=0

for i in heightdata:
    total=total+i

mean=total/n
print(mean)

heightdata.sort()

if(n%2!=0):
    median=heightdata[n//2]
else:
    median1=heightdata[n//2]
    median2=heightdata[n//2+1]
    median=(median1+median2)/2

print(median)

mode=Counter(heightdata)
occurance=0
for i in mode.items():
    if(i.value>60 and i.value<70):
        occurance=occurance+1
print(occurance)


    
