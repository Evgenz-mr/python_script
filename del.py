import os
import time

now = time.time()

f = "D:\\tasks\\t"
for i in os.listdir(f):
    if os.stat(os.path.join(f, i)).st_mtime < now - 1 * 86400:
        os.remove(f+'\\'+i)
