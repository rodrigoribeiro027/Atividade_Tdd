class Triangle:
    def check_triangle(self, a: int, b: int, c: int) -> str:
        if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
            return "Não é um triângulo válido"
        elif a == b == c:
            return "Triangulo Equilatero"
        elif a == b or a == c or b == c:
            return "Triangulo Isosceles"
        else:
            return "Triangulo Escaleno"