
n = int(input('Введите шестизначный номер вашего билета: '))

b = n//1000

one = b // 100
two = b // 10 % 10    
three = b % 10

c = n % 1000

four = c // 100
five = c // 10 % 10
six = c % 10

if (one+two+three)==(four+five+six):
    print ('Билет счастливый! Загадай желание и съешь его.')
else:
    print ('Билет обычный.')