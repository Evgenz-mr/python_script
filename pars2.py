import os

fw = "D:\\logs"
word = 'error'


for root, dir, files in os.walk(fw):
    for file in files:
        with open(fw+"\\"+file) as log:
            for line in log.readlines():
                if word in line:
                    print(file + " ---> " + line)
