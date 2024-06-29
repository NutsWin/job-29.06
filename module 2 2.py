first = input('Введите первое число: ') # число 123 и 42
print(first)
second = input('Введите второе число: ') # число 456 и 69
print(second)
third = input('Введите третье число: ') # число 789 и 42
print(third)

if first == second or second == third or first == third:
    print( 2 )
elif first == second == third:
    print( 3 )
elif first != second != third:
    print( 0 )







