# Import os module,This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
#Import for converting date format
import datetime
#open csv 
csvpath=os.path.join('Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
# skipping Header
    csv_header=next(csvreader)
#Setting up variable
    totalprofitloss=0
    lengthFile=0
    data=[]
    month=[]
#creating list by appending 
    for row in csvreader:
        data.append(float(row[1]))
        month.append(row[0])
    grtinc=0
    grtdec=0
#Finding greatest increase and decrease
    for i in range(0,len(data)-1):
#Greatest Increase
        if(data[i+1]-data[i]>grtinc):
            grtinc=data[i+1]-data[i]
            monthinc=month[i+1]
#Greatest decrease
        elif(data[i+1]-data[i])<grtdec:
            grtdec=data[i+1]-data[i]
            monthdec=month[i+1]
#Total profit
    totalprofit=int(sum(data))
#Average change
    firstrow=int(data[0])
    lastrow=int(data[-1])
    lengthrow=len(data)
    aveagechange=(lastrow-firstrow)/(lengthrow-1)
#Changing Datetime format
    montincformat=datetime.datetime.strptime(monthinc,'%b-%y')
    montdecformat=datetime.datetime.strptime(monthdec,'%b-%y')

file_output=open("PyBank_output.txt",'w')
#writing output file
file_output.write("Financial Analysis\n")
file_output.write("----------------------------\n")
file_output.write("Total Months:"+str(lengthrow)+"\n")
file_output.write("Total: $"+str(totalprofit)+"\n")
file_output.write("Average  Change: $"+str(round(aveagechange,2))+"\n")
file_output.write("Greatest Increase in Profits: "+str(datetime.date.strftime(montincformat,'%b-%Y'))+" ($"+str(round(grtinc))+")\n")
file_output.write("Greatest Increase in Profits: "+str(datetime.date.strftime(montdecformat,'%b-%Y'))+" ($"+str(round(grtdec))+")\n")
#Displaying the output
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:{lengthrow}")
print(f"Total: ${totalprofit}")
print(f"Average  Change: ${round(aveagechange,2)}")
print(f"Greatest Increase in Profits: {datetime.date.strftime(montincformat,'%b-%Y')} (${round(grtinc)})")
print(f"Greatest Decrease in Profits: {datetime.date.strftime(montdecformat,'%b-%Y')} (${round(grtdec)})")
     
