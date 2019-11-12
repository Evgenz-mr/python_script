# # # # # # # # # # # # #
#                       #
# python version 3.7.3  #
#                       #
# # # # # # # # # # # # #

import subprocess
import datetime
import time
import os


fname = "/opt/log_network.txt"
if not os.path.exists(fname) == True:
    tm = open(fname, 'w')
    tm.close()

fl = open(fname, 'a')

zone = ['Ryazan', 'Moskow', 'All regions']
rzn = ['рязань', 'Рязань', '1']
msk = ['Москва', 'москва', '2']
al = ['все', 'Все', 'всё', 'Всё', '3', 'all']


def net(a, b, ip_n, m=0): # a & b == >> vars for range, ip_n == >> adress 3 - oktets (IP), m - choose region
    global fl
    global zone
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
    print('\n' + '\n' + ' ' * 8 +  '=' * 25 + '>>' + ' ' + f"'Region is: {zone[m]}'" + ' ' + '<<' + '=' * 25, file=fl)
    print('\n' + ' ' * 4 +  '=' * 25 + '>>' + ' ' + 'Time is: ' + st + ' ' + '<<' + '=' * 25 + '\n' + ' ' * 63, file=fl)
    with open(os.devnull, "w") as limbo:
        for n in range(a, b + 1):
            ip = f"{ip_n}.{n}" # example 192.168.145.{n} (n ==> range(0, 100))
            result = subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                                      stdout=limbo, stderr=limbo).wait()
            if result:
                print(' ' *  62, ip, "inactive", file=fl)
            else:
                print(' ' * 4, ip, "active", file=fl)



choose_region = input("Выберите регион: Рязань(1), Москва(2), Все(3): ")

if choose_region in rzn:
    net(250, 254, ip_n="192.168.145", m=0)
    print("Выполнено!")
elif choose_region in msk:
    net(240, 250, ip_n="192.168.145", m=1)
    print("Выполнено!")
elif choose_region in al:
    net(240, 254, ip_n="192.168.145", m=2)
    print("Выполнено!")
else:
    print(f"Указанный регион: >> {choose_region} << не определен в программе")

fl.close()
