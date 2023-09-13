#ruslan=input('камень - 1, бумага - 2, ножницы - 3 (введите число от 1 до 3) - ')
#timur=input('камень - 1, бумага - 2, ножницы - 3 (введите число от 1 до 3) - ')
#instrum=['1','2','3']
#if (ruslan in instrum) and (timur in instrum):
#    if ruslan == timur:
#        print('ничья')
#    elif timur > ruslan:
#        print('Руслан победил')
#    elif timur==1 and ruslan==3:
#        print('Руслан победил')
#    else:
#        print('Тимур победил')
#else:
#    print('неверно введеные данные')

instrum = ['камень', 'ножницы', 'бумага']

nichia = ['ножницыножницы','бумагабумага', 'каменькамень']
win = ['ножницыбумага', 'бумагакамень', 'каменьножницы']
lose = ["бумаганожницы","ножницыкамень", "каменьбумага"]


ruslan = input('Руслан вводит камень, бумага или ножницы - ').lower()
timur = input('Тимур вводит камень, бумага или ножницы - ').lower()

suminstr = ruslan+timur

if ruslan and timur in instrum:
    if suminstr in win:
        print('Победил Руслан')
    elif suminstr in lose:
        print('победил Тимур')
    else:
        print('Ничья')
else:
    print('неправильно введено слово!')
