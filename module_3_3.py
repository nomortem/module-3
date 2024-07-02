def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(10)
print_params(10, 'другая строка')
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [100, 'women', False]
values_dict = {'a': 200, 'b': 'dictionary', 'c': [4, 5, 6]}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
