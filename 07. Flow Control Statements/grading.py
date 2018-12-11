lst = [int(x) for x in input('Enter marks in three subjects: ').split()]

failed = False

for x in lst:
    if x < 35:
        failed = True

if failed:
    print('Student is failed.')
else:
    a, b, c = lst
    avg = (a + b + c) / 3
    grade = ''

    if avg <= 59:
        grade = 'C'
    elif avg <= 69:
        grade = 'B'
    else:
        grade = 'A'

    print('Student obtained ', grade, ' grade.')
