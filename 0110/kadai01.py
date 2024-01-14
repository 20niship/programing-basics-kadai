import sympy

sympy.init_printing()
x = sympy.Symbol('x')

H_list = []
H_list.append(1)
H_list.append(2*x)
for i in range(2, 10):
    H_list.append(2*H_list[i-1]*x - 2*i*H_list[i-2])

print(H_list.pop())


