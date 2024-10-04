import chardet

# pip install chardet
# rb - odczyt bajtowy
with open('test.log', 'rb') as f:
    raw_data = f.read()

print(raw_data)
# b'Powitanie\r\nKolejne\r\nKolejne\r\nDopisane\r\nDopisane\r\nDopisane\r\nDopisane\r\nDo\xc5\x9bdane\r\n'
# b - dane bajtowego
# \xc5 - zapis szesnastkowy wartości 197 dziesiętnie
# \x9b

result = chardet.detect(raw_data)
print(result)  # {'encoding': 'MacRoman', 'confidence': 0.6479775280898876, 'language': ''}
# po dodaniu wiekszej ilości polskich znaków
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
print(result['encoding'])  # encoding
encoding = result['encoding']
print(raw_data.decode(encoding=encoding))
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
# utf-8
# Powitanie
# Kolejne
# Kolejne
# Dopisane
# Dopisane
# Dopisane
# Dopisane
# Dośdane
# Dośąźćdane
