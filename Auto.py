from Circle import Circle
from Figure import Figure
from Quadrate import Quadrate
from Triangle import Triangle
from Trapezoid import Trapezoid
from Rectangle import Rectangle
from turtle import *


class Auto:
    def __init__(self, fuel_c, km, fuel, *parts):
        self._fuel_consumption = fuel_c
        self._km = km
        self._fuel = fuel
        self.parts: list[Figure] = list(parts)

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
        i = 1
        if self._km >= 1000:
            i = 1 + (self._km // 1000) * 0.01
        self._fuel_consumption = self._fuel_consumption * i
        return self._fuel_consumption

    def ShowFuel(self):
        self.calculate_fuel()
        self._fuel = self._fuel - self._fuel_consumption * self._km
        return self._fuel

    def AddFuel(self, litrs):
        self._fuel = self._fuel + litrs
        return self._fuel

    def PrintData(self):
        print(f'fuel {self._fuel}, fuel_consumption {self._fuel_consumption}, km {self._km}')

    def Go(self):
        #for _ in range(self._km):
            #for part in self.parts:
                #part.move(1, 0)
                #update()
        self.calculate_fuel()
        if self._fuel < self._fuel_consumption * (self._km / 100):
            print('Not enough fuel. Add? Y/N')
            res = input()
            if res == 'Y':
                print('How much? In litres')
                f = int(input())
                self.AddFuel(f)
                self.Go()
            elif res == 'N':
                print("you can't go")
        else:
            print('you can go')






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

    bmw = Auto(1, 2000, 10000, body, roof, wheel1, wheel2, wheel1part, wheel2part, window1, window2)

    tracer(0, 0)

    bmw.show()
    bmw.Go()
    bmw.PrintData()
    mainloop()