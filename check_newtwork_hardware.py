import paramiko


class SSH:
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

    def exec_cmd(self, cmd):
        ''' Необходимо выполнить команду с помощью скрипта (interface print)'''
        stdin, stdout, stderr = self.client.exec_command(cmd)
        data = stdout.read() + stderr.read()
        if not stderr:
            raise stderr
        return data.decode()


if __name__ == '__main__':
    with SSH(hostname='10.10.10.254', username='usver', password='passwd', port=22) as ssh:  # noob@10.0.1.**
        out = ssh.exec_cmd('interface print')
        print(out)
        print(out, file=open('D:\\tasks\\log.txt', 'a'))  # и записью вывода в лог
