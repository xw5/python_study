tel = {'jack': 4098, 'sape': 4139}
for k, v in tel.items():
    print(k, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
result = zip(questions, answers)
print(result)
for q, a in result:
    print('What is your {0}?  It is {1}.'.format(q, a))
