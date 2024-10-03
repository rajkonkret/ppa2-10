# od Python 3.10
# match case

lista = []
lang = input("Podaj znany Ci język programowania")

match lang.lower().strip():
    case "python":
        lista.append("Znam Pythona")
    case "java":
        lista.append("Znam Javę")
    case _:  # wartość domyślna, else, inne
        print("Nie znam takiego języka")

print(lista)
# Podaj znany Ci język programowaniajava
# ['Znam Javę']
