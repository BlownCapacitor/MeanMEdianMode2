import math
import csv
from collections import Counter

with open('heightweight.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
data.pop(0)
newData = []

for i in range(len(data)):
    num = data[i][2]
    newData.append(float(num))
n = len(newData)
sum = 0
for x in newData:
    sum = sum + x
mean = sum/n
print("mean:" ,mean)

newData.sort()
if n % 2 == 0:
    median1 = float(newData[n//2])
    median2 = float(newData[n//2-1]) 
    median = median1 + median2 // 2  
else:
    median = newData[n//2]

print("median:" ,median)

data1 = Counter(newData)
mode_data_for_range = {
                        
                        "100-110": 0,
                        "110-120": 0,
                        "120-130":0,
                        "130-140":0,
                        "140-150":0,
                        "150-160":0
                        
                    }
for weight, occurence in data1.items():
    if 100 < float(weight) < 110:
        mode_data_for_range["100-110"] += occurence
    elif 110 < float(weight) < 120:
        mode_data_for_range["110-120"] += occurence
    elif 120 < float(weight) < 130:
        mode_data_for_range["120-130"] += occurence
    elif 130 < float(weight) < 140:
        mode_data_for_range["130-140"] += occurence
    elif 140 < float(weight) < 150:
        mode_data_for_range["140-150"] += occurence
    elif 150 < float(weight) < 160:
        mode_data_for_range["150-160"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)

print("mode:" ,mode)


