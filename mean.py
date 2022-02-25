import csv

with open('data.csv',newline='') as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    num = filedata[i][2]
    newdata.append(float(num))

n=len(newdata)
total=0

for i in newdata:
    total+=i

mean=total/n
print('mean is :'+ str(mean))