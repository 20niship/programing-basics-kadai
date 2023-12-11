import math

class Matrix:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def add(self,other):
        result = Matrix(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)
        return result
    
    def mul(self, other):
        result = Matrix(
            self.a * other.a + self.b * other.c, 
            self.a * other.b + self.b * other.d,
            self.c * other.a + self.d * other.c,
            self.c * other.b + self.d * other.d
            )
        return result

    def __truediv__(self, other):
        result = Matrix(self.a / other, self.b / other, self.c / other, self.d / other)
        return result

    def __matmul__(self, other):
        return self.mul(other)

    def __add__(self, other):
        return self.add(other)

    def __repr__(self):
        return f"[{self.a},  {self.b}]\n[{self.c},  {self.d}]"   

    def MatrixExp(self, n=1000):
        result = Matrix(0,0,0,0)
        for i in range(1,n):
            tmp = self
            for k in range(i-1):
                tmp = tmp @ self
            result += tmp / math.factorial(i)
        return result

if __name__ == '__main__':
    m = Matrix(1,2,3,4)
    print(m.MatrixExp())


