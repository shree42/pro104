import csv
from collections import Counter

with open('data.csv',newline='') as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    num = filedata[i][2]
    newdata.append(float(num))

data=Counter(newdata)
mode_data_for_range={
    "100-120":0,
    "120-140":0,
    "140-180":0
}

for weight,occurence in data.items():
    if(100<float(weight)<120):
        mode_data_for_range["100-120"] +=occurence
    elif(120<float(weight)<140):
        mode_data_for_range["120-140"]+=occurence
    elif(140<float(weight)<180):
        mode_data_for_range["140-180"]+=occurence

mode_range,modeOccurence=0,0
for ranges,occurence in mode_data_for_range.items():
    if(occurence>modeOccurence):
        mode_range,modeOccurence=[int(ranges.split("-")[0]),int(ranges.split('-')[1])],occurence

mode=float((mode_range[0]+mode_range[1])/2)

print(mode)

