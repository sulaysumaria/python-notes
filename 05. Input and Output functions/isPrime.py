isPrime = True

number = int(input('Enter a number: '))

for x in range(2, number-1):
    if number % x == 0:
        isPrime = False

if(isPrime):
    print('Number is prime.')
else:
    print('Number is not Prime.')
