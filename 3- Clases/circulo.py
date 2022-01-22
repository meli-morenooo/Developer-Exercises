import math
class Circulo():
    def __init__(self, radio):
        if isinstance(radio,(int, float)) and not radio <= 0:
            self.r = radio
        else:
            print("El radio debe ser mayor a cero.")
            exit()

    def setRadio(self):
        return self.r
    
    def getArea(self):
        self.pi = math.pi
        self.a = round(self.pi * (self.r*self.r),2)
        return self.a
    
    def getPerimetro(self):
        self.p = round(2 * self.pi * self.r,2)
        return self.p

    def __str__(self):
        return "\nRadio: " + str(self.setRadio()) + "\nArea: " + str(self.getArea()) + "\nPerimetro: " + str(self.getPerimetro()) + "\n"

    def __mul__(self, obj):
        n = self.r * obj.r
        r = Circulo(n)
        return r


def main():
    a = Circulo(10)
    # b = Circulo(0)
    b = Circulo(36)
    c = a * b
    print(c)
    

if __name__ == '__main__':
    # c = Circulo(0)
    # c = Circulo(-5)
    # c = Circulo(5)
    main()