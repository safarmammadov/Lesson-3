print ('Привет')
while True:
        print ('введите число А')
        A = int(input())
        print ('введите число B')
        B = int(input())
        Mult = A * B
        Devis = A / B
        Summ = A + B
        Sub = A - B
        if A * B <= 0:
                print('Значение должны быть больше 0')
        else:
                print(f'Умножение: {Mult}')
                print(f'Деление: {Devis}')
                break
else:
        print('Значение должны быть больше 0')