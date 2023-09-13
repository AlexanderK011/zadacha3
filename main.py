ruslan=input('камень - 1, бумага - 2, ножницы - 3 (введите число от 1 до 3) - ')
timur=input('камень - 1, бумага - 2, ножницы - 3 (введите число от 1 до 3) - ')
instrum=['1','2','3']
if (ruslan in instrum) and (timur in instrum):
    if ruslan == timur:
        print('ничья')
    elif timur > ruslan:
        print('Руслан победил')
    elif timur==1 and ruslan==3:
        print('Руслан победил')
    else:
        print('Тимур победил')
else:
    print('неверно введеные данные')