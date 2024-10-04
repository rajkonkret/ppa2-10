# funkcja zagnieżdzona
# uzywana w dekoratorach

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2


fun1()  # To jest fun1
xFun = fun1()
print(type(xFun))  # <class 'function'>
print(xFun)  # <function fun1.<locals>.fun2 at 0x00000246C6FD9EE0>
# nazwa funkcji i nawiasy ()
xFun()  # To jest fun2
