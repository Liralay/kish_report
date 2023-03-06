import pandas as pd

day = int(input("За какой день отчет: "))
if day//10 == 0:
    day == int(("0" + str(day)))
else:
    pass

month = int(input("За какой месяц отчет (например 03 - март): "))
if month//10 == 0:
    month == int(("0" + str(day)))
else:
    pass

hour = int(input("В каком часу было первое сканирование?\nВ будни выставка открывается в 12, а в выходные в 11: "))



first_scan = f"2023-{int(month)}-{int(day)} {hour}:00:00+03"
end_of_the_day = f'2023-{int(month)}-{int(day)} 22:00:00+03'

df = pd.read_excel("total_report.xlsx")

df['Время сканирования'] = pd.to_datetime(df['Время сканирования'], format='%Y-%m-%d %H:%M:%S+03', errors='coerce')

df = df[df['Время сканирования'] >= pd.to_datetime(first_scan, format='%Y-%m-%d %H:%M:%S+03')]

df = df[df['Время сканирования'] <= pd.to_datetime(end_of_the_day, format='%Y-%m-%d %H:%M:%S+03')]


df = df[df['Статус СКД билета'] == 'Внутри']

df = df[df['Дата/время возврата'].isna()]

free_tickets = (df['Сумма продажи'] == 0).sum()
print("\n")
print(f'Проходов по бесплатным билетам: {free_tickets}')

if '31.05.2023 22:00:00' in df['Дата/время события'].values:
    count = ((df['Дата/время события'] == '31.05.2023 22:00:00')).sum()
    print(f"Количество билетов пресейла: {count - free_tickets}")
else:
    print("Количество билетов пресейла: 0")

num_rows = df.shape[0]
print("Всего проходов за сегодня: ", num_rows)