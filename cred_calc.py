# import pandas as pd
#
# # intialise data of lists.
# data = {'Name': ['Tom', 'nick', 'krish', 'jack', 'Evgen'],
#         'Age': [a for a in range(20, 25)]}
#
# # Create DataFrame
# df = pd.DataFrame(data)
#
# # Print the output.
# print(df)


####
####
# Import pandas package
# import pandas as pd
#
# # Define a dictionary containing employee data
# data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
#         'Age': [27, 24, 22, 32],
#         'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
#         'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}
#
# # Convert the dictionary into DataFrame
# df = pd.DataFrame(data)
#
# # select two columns
# print(df)


######
######
# расчет переплаты процентов за кредит

# import webbrowser
# import re
#
# call = input('Введите ссылку или запрос: ')
# if re.search(r'\.', call):
#     webbrowser.open_new_tab('https://' + call)
# elif re.search(r'\ ', call):
#     webbrowser.open_new_tab('https://yandex.ru/search/?text='+call)
# else:
#     webbrowser.open_new_tab('https://yandex.ru/search/?text='+call)

def credit():
    cred = float(input("Введите сумму стоимости автомобиля: "))
    self_sum = float(input("Введите сумму первого взноса: "))
    sm = cred - self_sum
    st = input("Введите процент годовой ставки: ")
    st = st.replace(",", ".")
    st_percent = float(st) / 100
    year = float(input("Введите срок кредита (в годах): "))
    sum_pog = float(input("Введите сумму остаточного платежа: "))
    sum_main = 0
    if sum_pog == '':
        sum_pog = sum_main
    st_cred = (year * st_percent * sm + sm - sum_pog) // (year * 12)
    print(f"Проценты переплаты за {int(year)} года/лет: "
          + (str(float(st_percent * year * (cred - sum_pog))) + (str(" рублей"))))
    print(f"Ежемесяцный платеж: {st_cred}" + " рублей")
    print(f"Остаточный платеж: {sum_pog}")


ans = ['да', 'yes', 'y']

while True:
    credit()
    ex = input("Хотите повторить оперцию ?: ")
    if ex not in ans:
        break

# import sys
#
# message = ' '.join(sys.argv[1:]) or "Hello World!"
# channel.basic_publish(exchange='',
#                       routing_key='hello',
#                       body=message)
# print(" [x] Sent %r" % message)

# import requests
# from bs4 import BeautifulSoup
# import csv
# # pip install beautifulsoup4
# # pip install lxml
#
# def get_html(url):
#     r = requests.get(url)    # Получим метод Response
#     r.encoding = 'utf8'
#     return r.text   # Вернем данные объекта text
#
#
# def csv_read(data):
#     with open("data.csv", 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow((data['head'], data['link']))
#
# def get_link(html):
#     soup = BeautifulSoup(html, 'lxml')
#     head = soup.find('div', id='section-content').find_all('a', class_="entry-header")
#     for i in head:
#         link = 'https://ru.investing.com/equities/gazprom_rts' + i.get('href')
#         heads= i.find('h1').string
#         data = {'head': heads,
#                  'link': link}
#         csv_read(data)
#
#
# data = get_link(get_html('https://ru.investing.com/equities/gazprom_rts'))
# #https://3dnews.ru/news
