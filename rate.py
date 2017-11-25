""" task 3 """
# Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

school_classes = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
                  {'school_class': '4b', 'scores': [2, 4, 3, 5, 4]},
                  {'school_class': '5a', 'scores': [5, 5, 5, 5, 4]},
                  {'school_class': '6a', 'scores': [4, 2, 3, 2, 5]},
                  {'school_class': '7a', 'scores': [5, 5, 4, 5, 3]},
                  {'school_class': '7b', 'scores': [5, 1, 4, 5, 3]},
                 ]

total_avg = []

for class_item in school_classes:
    rates = class_item['scores']
    total_avg += rates
    avg_rate = sum(rates) / len(rates)
    print(class_item['school_class'], ':', avg_rate)

print('Average rate: ', round(sum(total_avg) / len(total_avg), 1))
