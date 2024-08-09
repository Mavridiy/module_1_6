my_dict = {'Иван' : 1985, 'Мария' : 1993, 'Антон' : 1999}
print('Dict: ', my_dict)
print('Existing: ', my_dict['Мария'])
print('Not existing: ', my_dict.get('София'))
my_dict['София'] = 2005
my_dict['Ольга'] = 1986
del my_dict['Антон']
print('Modified: ', my_dict)

my_set = {1, 2, 6, 2, 1, 6, 5, 5, 1, 'a', 'a'}
print('Set: ', my_set)
my_set.add(7)
my_set.add(8)
print('First Modified: ', my_set)
my_set.discard('a')
print('Second Modified: ', my_set)
