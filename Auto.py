from Circle import Circle
from Lab_06.Figure import Figure
from Quadrate import Quadrate
from Triangle import Triangle
from Trapezoid import Trapezoid
from Rectangle import Rectangle
from turtle import *


class Auto:
    def __init__(self, *parts, fuel_c, km, fuel):
        self.parts: list[Figure] = list(parts)
        self._fuel_consumption = fuel_c
        self._km = km
        self._fuel = fuel

    def show(self):
        for part in self.parts:
            part.show()

    def hide(self):
        for part in self.parts:
            part.hide()

    def move(self, dx, dy):
        for part in self.parts:
            part.move(dx, dy)

    def calculate_fuel(self):
        pass

    def ShowFuel(self):
        pass

    def AddFuel(self):
        pass

    def PrintData(self):
        pass

    def Go(self):
        pass



if __name__ == '__main__':
    x = 0
    y = 0

    body = Rectangle(x, y, x + 200, y + 70, 'red')
    roof = Trapezoid(x + 20, y + 70, 150, 100, 'lime')
    wheel1 = Circle(x + 40, y - 30, 30, 'blue')
    wheel2 = Circle(x + 160, y - 30, 30, 'blue')
    wheel1part = Triangle(x + 40, y - 30, 10, 'magenta')
    wheel2part = Triangle(x + 160, y - 30, 10, 'magenta')
    window1 = Quadrate(x + 60, y + 40, 30, 'lightblue')
    window2 = Quadrate(x + 120, y + 40, 30, 'lightblue')
    bmw = Auto(body, roof, wheel1, wheel2, wheel1part, wheel2part, window2, window1)

    tracer(0, 0)

    bmw.show()
    for _ in range(100):
        bmw.move(1, 0)
        update()
    mainloop()