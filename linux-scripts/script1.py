#!/usr/bin/python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# Write script that monitors certain log file for any "sudo" apperances
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with open("logi.txt", "a") as d:
            with open( "/var/log/auth.log","r") as f:
                changes = f.readlines()[-1]
                print(f'File modified: {changes}')
                d.write(f'File modified: {changes}\n')
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path='/var/log/auth.log', recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
