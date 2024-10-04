def connect(**opcje):  # ** - dowolna ilość argumentów nazwanych, argumenty słownikowe
    print(opcje)


connect()
connect(a=9)
connect(a=9, b=10)
# {}
# {'a': 9}
# {'a': 9, 'b': 10}
connect(name="Radek")  # {'name': 'Radek'}


def all_params(*args, **kwargs):
    print(args, kwargs)


all_params(1, 2, 3)
all_params(1, 2, 3, c=0, name="Radek")
# (1, 2, 3) {}
# (1, 2, 3) {'c': 0, 'name': 'Radek'}
all_params(1, 2, c=9)  # argumenty pozycyjne przed nazwanymi
# (1, 2, 3) {'c': 0, 'name': 'Radek'}
# (1, 2) {'c': 9}
