import matplotlib.pyplot as plt
import math
import numpy

def f(x):
    return 1.0 / (1.0 + x**2.0)

def interpolation(n, count=30):
    results = []
    x = numpy.linspace(-5, 5, n + 1)
    vander_x = numpy.vander(x, n + 1, True)
    coefficients = numpy.linalg.solve(vander_x, list(map(f, x)))
    
    check = numpy.linspace(-5, 5, count)
    
    for x in check:
        result = 0
        for index, coefficient in enumerate(coefficients):
            result += coefficient * (x ** index)
        results.append(result)

    return results

plt.plot(numpy.linspace(-5, 5, 30), interpolation(5))
plt.plot(numpy.linspace(-5, 5, 30), interpolation(10))
plt.plot(numpy.linspace(-5, 5, 30), interpolation(15))
plt.show()

function = []
for x in numpy.linspace(-5,5,30):
    function.append(f(x))

plt.plot(numpy.linspace(-5, 5, 30), function)
plt.show()

eps = []
for i in range(0, 30):
    eps.append(function[i] - interpolation(15,30)[i])


plt.plot(numpy.linspace(-5, 5, 30), eps)
plt.show()


