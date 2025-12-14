# In certain dir find how many lines with "WARNING" does all files have in it
import os

dir = "/home/vboxuser/test/log/"
warning_counts = {}

for filename in os.listdir(dir):
    fullpath = os.path.join(dir, filename)

    if os.path.isfile(fullpath):
        warning_count = 0

        try:
            with open(fullpath, "r", encoding="utf-8") as f:
                for line in f:
                    warning_count += line.count("WARNING")
        except (UnicodeDecodeError, OSError):
            continue

        warning_counts[filename] = warning_count

print(warning_counts)
