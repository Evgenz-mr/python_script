# -*- coding: UTF-8 -*-
import paramiko
import datetime
import time


class SSH():
    def __init__(self, **kwargs):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.kwargs = kwargs


    def __enter__(self):
        '''Метод подключения к удаленному хосту с импрортируемым модулем paramiko'''
        kw = self.kwargs
        self.client.connect(hostname=kw.get('hostname'), username=kw.get('username'),
                            password=kw.get('password'), port=int(kw.get('port', 22)))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def timeline(self, st):
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
        self.st = st
        return self.st

    def exec_cmd(self, cmd):
        ''' Необходимо выполнить команду с помощью скрипта (interface print)'''
        stdin, stdout, stderr = self.client.exec_command(cmd)
        data = stdout.read() + stderr.read()
        return data.decode()


if __name__ == '__main__':
    with SSH(hostname='10.20.10.254', username='usver', passwd', port=22) as ssh:  # usver@10.20.10.254
        out = ssh.exec_cmd('ip firewall filter print')   # команда выполняемая на устройстве
        res = ssh.timeline('%d-%m-%Y %H:%M:%S')   # формат времени
        print(out)
        print('  =========>> Time is: ' + res + ' ' + '<<=========' + '\n' + ' ' + '\n', out + '\n' +
              '//-------------------------------------------------------------------//',
              file=open('D:\\tasks\\log.txt', 'a'))  # и записью вывода в лог
