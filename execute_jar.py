import os

path = "C:\\Users\\18287736\Documents\\"
for roor, dir, files in os.walk(path):
    for file in files:
        if ".jar" in file:
            print((f"nohup java -jar {path}{file} > /dev/null 2>&1 &"))
            # запуск заглушек .jar в фоновом режиме(&)
            # os.system(f"nohup java -jar {path}{file} > /dev/null 2>&1 &")