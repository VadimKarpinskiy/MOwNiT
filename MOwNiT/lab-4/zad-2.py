from scipy import integrate as integ
import numpy as np
import math
import random

def f1(x):
    tmp = np.float_power(x,2) * (-1)
    return np.float_power(math.e, tmp) * np.float_power(math.log(x+1),2)

def f2(x):
    return 1 / (pow(x,3) - 2*x - 5)

def f3(x):
    return pow(x,5) * math.pow(math.e, -x) * math.sin(x)

def simpson(x,y):
    res = 0
    for i in range(len(x)-2):
        res += (1/6) * (x[i+1] - x[i]) * (y[i] + 4*y[i+1] + y[i+2])
    return res

def test():
    x = np.linspace(0, 10, 1000)
    y1 = [f1(xi) for xi in x]
    y2 = [f2(xi) for xi in x]
    y3 = [f3(xi) for xi in x]
    
    my_res = simpson(x,y1)
    lib_res = integ.simps(y1,x)
    print("Wartość wyliczona: ", my_res)
    print("Wartość funkcji bibliotecznej: ", lib_res)
    print("Błąd bezwzględny:", np.abs(lib_res - my_res))
    print("Błąd względny:", (np.abs(my_res - lib_res)/np.abs(lib_res)))

    print("------------------------------------------------------")

    my_res = simpson(x,y2)
    lib_res = integ.simps(y2,x)
    print("Wartość wyliczona: ", my_res)
    print("Wartość funkcji bibliotecznej: ", lib_res)
    print("Błąd bezwzględny:", np.abs(lib_res - my_res))
    print("Błąd względny:", (np.abs(my_res - lib_res)/np.abs(lib_res)))

    print("------------------------------------------------------")

    my_res = simpson(x,y3)
    lib_res = integ.simps(y3,x)
    print("Wartość wyliczona: ", my_res)
    print("Wartość funkcji bibliotecznej: ", lib_res)
    print("Błąd bezwzględny:", np.abs(lib_res - my_res))
    print("Błąd względny:", (np.abs(my_res - lib_res)/np.abs(lib_res)))





