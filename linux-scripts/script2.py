# Write script that monitors certain log file for any "sudo" apperances
import time
with open("/var/log/auth.log") as f:
    f.seek(0,2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(1)
            continue
        if "sudo" in line:
            print(line.strip())
