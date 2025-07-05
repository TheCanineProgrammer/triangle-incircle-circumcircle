import numpy as np
import matplotlib.pyplot as plt

class Line:
    def calculate_slope_intercept(self, P1 : tuple, P2 : tuple) -> list:
        x1, y1 = P1
        x2, y2 = P2
        if x1 == x2:
            return [None, None]
        elif y1 == y2:
            return [0, y1]
        m = (y1 - y2) / (x1 - x2)
        b = y1 - m * x1
        return [m, b]
    
    def calculate_length(self, P1 : tuple, P2 : tuple) -> float:
        x1, y1 = P1
        x2, y2 = P2

        return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

class Triangle(Line):

    def __init__(self, A : tuple, B : tuple, C : tuple):
        self.P1 = A
        self.P2 = B
        self.P3 = C
        self.dis = self.not_distinct()
        self.coll = self.check_collinearity()
        if self.dis or self.coll:
            raise ArithmeticError("No triangle can be made!")
        
        self.cx = (self.P1[0] + self.P2[0] + self.P3[0]) / 3
        self.cy = (self.P1[1] + self.P2[1] + self.P3[1]) / 3
        self.p = self.calculate_P()
        self.a, self.b, self.c = self.calculate_sides().values()
        self.A, self.B, self.C = self.calculate_angles().values()
        self.S = self.calculate_Area()
        self.r = self.calculate_r()
        self.R = self.calculate_R()

    def not_distinct(self) -> bool:
        if self.P1 == self.P2:
            return True
        elif self.P1 == self.P3:
            return True
        elif self.P2 == self.P3:
            return True
        return False
    
    def check_collinearity(self) -> bool:
        x1, y1 = self.P1
        x3, y3 = self.P3
        m, b = super().calculate_slope_intercept(self.P1, self.P2)

        if m == None:
            if x3 == x1:
                return True
            return False
        return True if abs(y3 - (m * x3 + b)) < 1e-9 else False                              # To avoid floating-point error

    def calculate_I(self) -> tuple:
        return ((self.P1[0] * self.a + self.P2[0] * self.b + self.P3[0] * self.c) / (self.a + self.b + self.c), (self.P1[1] * self.a + self.P2[1] * self.b + self.P3[1] * self.c) / (self.a + self.b + self.c))
    
    def calculate_Area(self) -> float:
        
        return np.sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))
    
    def calculate_P(self) -> float:
        a, b, c = self.calculate_sides().values()
        return (a + b + c) / 2

    def calculate_r(self) -> float:
        return self.S / self.p
    
    def calculate_R(self):
        return (self.a * self.b * self.c) / (4 * self.S)
    
    def calculate_sides(self) -> dict:
        return {"a" : super().calculate_length(self.P2, self.P3), "b" : super().calculate_length(self.P1, self.P3), "c" : super().calculate_length(self.P1, self.P2)}

    def calculate_angles(self) -> dict:
        A = np.degrees(np.arccos(np.clip((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c), -1.0, 1.0)))
        B = np.degrees(np.arccos(np.clip((self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c), -1.0, 1.0)))
        C = np.degrees(np.arccos(np.clip((self.a**2 + self.b**2 - self.c**2) / (2 * self.a * self.b), -1.0, 1.0)))
        return {"A" : A, "B" : B, "C" : C}

    def calculate_circumcenter(self) -> tuple:
        x1, y1 = self.P1
        x2, y2 = self.P2
        x3, y3 = self.P3

        D = 2 * (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))

        X = ((x1**2 + y1**2)*(y2 - y3) + (x2**2 + y2**2)*(y3 - y1) + (x3**2 + y3**2)*(y1 - y2)) / D
        Y = ((x1**2 + y1**2)*(x3 - x2) + (x2**2 + y2**2)*(x1 - x3) + (x3**2 + y3**2)*(x2 - x1)) / D

        return (X, Y)
    
    def vertices(self):
        return {"A" : self.P1, "B" : self.P2, "C" : self.P3}
    
    def save(self, name = "LOG"):
        with open(name + ".txt", "w") as log:
            log.write(f"A = {self.A}°, B = {self.B}°, C = {self.C}°\n")
            log.write(f"a = {self.a}, b = {self.b}, c = {self.c}\n")
            log.write(f"Area = {self.S}\n")
            log.write(f"2P = {self.p * 2}\n")
            log.write(f"Inradius: {self.r}\n")
            log.write(f"Incenter: {self.calculate_I()}\n")
            log.write(f"Circumradius: {self.R}\n")
            log.write(f"Circumcenter: {self.calculate_circumcenter()}\n")