#/usr/bin/python
# Write script that finds all .log files in
# "path" and writes its name and number of lines containing "ERROR"
import os

path = "/home/vboxuser/log_dir"
dir={}

for i in os.listdir(path):
    name = i
    if name.endswith(".log"):
        with open(os.path.join(path,name),"r") as p:
            for a in p:
                suma= sum(1 for line in p if "ERROR" in line or "Error" in line)
        dir[i] = suma

print(dir)
