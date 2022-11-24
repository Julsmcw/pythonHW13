tickets = int(input('Введите количество билетов: '))
result = []
for i in range(tickets):
    age = int(input(f'Введите возраст для билета {i+1}: '))
    if age < 18:
        ticket1 = int(0)
        print(f'Стоимость Вашего билета {ticket1} тугриков!')
    elif 18 <= age <= 24:
        ticket2 = int(990)
        result.append(ticket2)
        print(f'Стоимость Вашего билета {ticket2} тугриков!')
    else:
        ticket3 = int(1390)
        result.append(ticket3)
        print(f'Стоимость Вашего билета {ticket3} тугриков!')
if tickets >= 3:
    print('Стоимость билетов, с учетом скидки, составляет ', sum(result) * 0.9, 'тугриков!')
else:
    print('Стоимость билетов', sum(result), 'тугриков!')
