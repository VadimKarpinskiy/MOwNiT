import numpy as np
import random
import time

def matrix_generator(N):
    X = np.random.randint(-30, 30, (N, N)).astype(float)        # macierz współczynników
    RES = np.random.randint(-20, 20, N).astype(float)           # macierz wyrazów wolnych
    return X, RES


def gauss_jordan(X,RES):
    n = len(RES)
    for i in range(n):
        max_el_row = i      #numer wiersza największego elementu w kolumnie
        for j in range(i+1, n):
            if abs(X[j][i]) > abs(X[i][i]):
                max_el_row = j
        X[[i, max_el_row]] = X[[max_el_row, i]]                 # zamieniamy wiersze 
        RES[j], RES[i] = RES[i], RES[j]                         # zamieniamy wyrazy wolne
    
    for i in range(n):
        coeff = X[i][i]
        X[i] /= coeff         #tworzenie 1 na diagonali
        RES[i] /= coeff
        for j in range(n):
            if i != j:
                coeff = X[j][i]
                X[j] -= X[i] * coeff
                RES[j] -= RES[i]*coeff
    return RES

def check():
    a,b = matrix_generator(5)
    print_matrix(a)
    print("Kolumna wyrazów wolnych: ")
    print(b)
    result = gauss_jordan(a,b)
    truth = np.linalg.solve(a,b)
    for i in range(5):
        if result[i] != truth[i]:
            return False
    return True

def print_matrix(m):
    print("Macierz współczynników: ")
    for i in range(len(m)):
        for j in range(len(m)):
            print(m[i][j], end=" ")
        print()

def comparison():
    stat = []
    for i in range(10):
        N = random.randint(500,1000)
        X,RES = matrix_generator(N)

        start1 = time.time()
        L = np.linalg.solve(X,RES)
        end1 = time.time()

        start2 = time.time()
        K = gauss_jordan(X,RES)
        end2 = time.time()

        stat.append(((end1-start1),(end2-start2),N))

    for i in range(10):
        print("Rozmiar macierzy: ", stat[i][2], end="  ")
        print("Czas działania własnej funkcji (w sekundach): ", stat[i][1], end="  ")
        print("Czas działania funkcji bibliotecznej (w sekundach): ", stat[i][0])

print(check())
comparison()
    


