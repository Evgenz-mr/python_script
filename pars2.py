import os

fw = "D:\\configs"
word = 'route'

if os.path.exists(fw):
    for root, dir, files in os.walk(fw):
        for file in files:
            with open(fw+"\\"+file) as log:
                for line in log.readlines():
                    if word in line:
                        print(file+" ---> "+line)

raise ValueError("Not found dir")
