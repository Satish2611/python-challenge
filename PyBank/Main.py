import os
import csv
from itertools import tee

csvpath=os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)
    csvreader1,csvreader2,csvreader3=tee(csvreader,3)
    totalprofitloss=0
    lengthFile=0
    data=[]
    for row in csvreader1:
        data.append(float(row[1]))
    grtinc=0
    grtdec=0
    for i in range(0,len(data)-1):
        if(data[i+1]-data[i]>grtinc):
            grtinc=data[i+1]-data[i]
        elif(data[i+1]-data[i])<grtdec:
            grtdec=data[i+1]-data[i]
    totalprofit=sum(data)
    firstrow=int(data[0])
    lastrow=int(data[-1])
    lengthrow=len(data)
    aveagechange=(lastrow-firstrow)/(lengthrow-1)
    print(grtdec)
    print(round(grtinc))
    print(round(aveagechange,2))
    print (lengthrow)
    print (totalprofit)
    
    
