#!/usr/bin/python

# Write script that runs Linux command "df -h", parses the result,
# Writes onyl those partitions that uses >  40%

import subprocess

from orca.messages import percentage

result = subprocess.run(['df','-h'], capture_output=True,text=True)

lines = result.stdout.splitlines()
for i in lines:
    percentage = 40
    while percentage < 100:
        if str(percentage)+'%' in i:
            print(i.split()[0])
            break
        percentage +=1