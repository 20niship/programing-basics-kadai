import sympy
from math import pi,sqrt, factorial, exp

sympy.init_printing()
x = sympy.Symbol('x')

H_list = []
H_list.append(1)
H_list.append(2*x)

MAX = 20 

for i in range(2, MAX):
    H_list.append(2*H_list[i-1]*x - 2*i*H_list[i-2])

def inner_pod(m,n):
    assert m >= 0 and n >= 0
    assert m <= MAX and n <= MAX
    Hm = H_list[m]
    Hn = H_list[n]
    sympy.integrate(Hm*Hn*exp(-x**2), (x, -1000, 1000))

def calc_answer(m,n):
    if m != n:
        return 0
    return sqrt(pi)*(2**n) * factorial(n)


m = n = 10
expected = calc_answer(m,n)
print(expected)
ans = inner_pod(m,n)
print(ans)

