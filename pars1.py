import os.path

#Запрос ввода расположения лога который будем парсить
name_log = input('Введите расположение и имя лог файла: ')

if os.path.exists(name_log) == True:
###Запрос слова по которому будем парсить лог
   word = input('Введите слово: ')
###Открываем файл для записи парсинга лог файла
   log = open('/opt/python_scripts/pars', 'w')
   print('Отчет сохранен в директории /opt/python_scripts/pars')
   with open(name_log) as logfile:
      for line in logfile.readlines():
         if word in line:   
            print(line, file=log)
else:
   print('Указанной директории не существует')
