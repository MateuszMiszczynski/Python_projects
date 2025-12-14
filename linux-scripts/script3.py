# Write scipt that finds if "file" exists in certain dir
import os
import sys

path = "."
file = 'config.yaml'
def file_exists(path,file):
    if os.path.isfile(file):
        sys.exit(0)
    else:
        print("File not found")
        sys.exit(1)

file_exists(path,file)