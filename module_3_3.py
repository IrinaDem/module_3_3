def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print("Примеры вызовов print_params:")
print_params()
print_params(10)
print_params(10, 'новая строка')
print_params(b=25)
print_params(c=[1, 2, 3])

print("\nРаспаковка параметров:")
values_list = [3.14, 'hello', False]
values_dict = {'a': 42, 'b': 'world', 'c': None}

print_params(*values_list)
print_params(**values_dict)

print("\nРаспаковка + отдельные параметры:")
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, c=42)

def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
    list_my.append(item)
    return list_my

my_list = append_to_list(1)
my_list = append_to_list(2, my_list)
my_list = append_to_list(3)
print("\nСодержимое списка:", my_list)
