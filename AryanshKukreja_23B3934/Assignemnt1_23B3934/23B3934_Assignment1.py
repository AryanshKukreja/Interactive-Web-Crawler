import os

f1 = open("/Users/aryanshkukreja/Downloads/data/testcase1/2008.txt", "r")
data1 = f1.read()
f2 = open("/Users/aryanshkukreja/Downloads/data/testcase1/2012.txt", "r")
data2 = f2.read()
f3 = open("/Users/aryanshkukreja/Downloads/data/testcase1/2016.txt", "r")
data3 = f3.read()

data4 = data1 + data2 + data3
lines = data4.split("\n")
split_data = []

for line in lines:
    split = line.strip().split('-')
    
    # Check if the entry has the expected number of elements
    if len(split) == 4:
        split_data.append(split)

for entry in split_data:
    entry[1] = int(entry[1])
    entry[2] = int(entry[2])
    entry[3] = int(entry[3])

aggregated_data = {}

for entry in split_data:
    country, gold, silver, bronze = entry[0], entry[1], entry[2], entry[3]
    aggregated_data.setdefault(country, [0, 0, 0])
    aggregated_data[country][0] += gold
    aggregated_data[country][1] += silver
    aggregated_data[country][2] += bronze


sorted_data1=dict(sorted(aggregated_data.items(),key=lambda x:(-x[1][0],x[0])))

print(sorted_data1)
