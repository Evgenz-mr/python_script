# # # # # # # # # # # # #
#                       #
# python version 3.7.3  #
#                       #
# # # # # # # # # # # # #


import datetime
import time
import os
import subprocess


fl = open("/opt/logs_1.txt", "a")


def rzn(a, b, ip_n): # a & b == >> vars for range, ip_n == >> adress 3 - oktets (IP)
    global fl
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
    print('\n' + ' ' * 4 +  '=' * 25 + '>>' + ' ' + 'Time is: ' + st + ' ' + '<<' + '=' * 25 + '\n' + ' ' * 63, file=fl)
    with open(os.devnull, "w") as limbo:
        for n in range(a, b):
            ip = f"{ip_n}.{n}" # example 192.168.145.{n} (n ==> range(0, 100))
            result = subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                                      stdout=limbo, stderr=limbo).wait()
            if result:
                print(' ' *  62, ip, "inactive", file=fl)
            else:
                print(' ' * 4, ip, "active", file=fl)


rzn(200, 255, ip_n="192.168.145")
fl.close()
