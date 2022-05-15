tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий',
    'Борис', 'Елена', 'Дмитрий', 'Дмитрий', 'Сергей',
    'Алексей', 'Ксения', 'Наталья', 'Владимир']

klasses = ['9А', '7В', '9Б', '9В', '8Б',
           '10А', '10Б', '9А', '10B', '11A']

tutor_klass_old = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
print(type(tutor_klass_old))

try:
    for i in range(len(tutors)):
        print(next(tutor_klass_old))
except:
    print((tutors[len(klasses)], None))
