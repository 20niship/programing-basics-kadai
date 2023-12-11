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

    def __repr__(self):
        return f"[{self.a},  {self.b}]\n[{self.c},  {self.d}]"   

if __name__ == '__main__':
    m1 = Matrix(1,2,5,1)
    m2 = Matrix(1,0,0,1)
    m3 = m1.add(m2)
    print(m3) 


