""" Task 1 """


age = int(input('Input your age, please: '))
if age < 7:
    print('You must be in kindergarten')
elif age >= 7 and age <= 18:
    print('You have to go to school')
elif age > 18 and age <= 23:
    print('You have to study at the Institute')
else:
    print('You have to work')
