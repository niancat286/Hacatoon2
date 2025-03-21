import math
from Figure import Figure
from Auto import Auto
from turtle import *
from Circle import Circle
from Quadrate import Quadrate
from Triangle import Triangle
from Trapezoid import Trapezoid
from Rectangle import Rectangle

class Truck(Auto):
    def init(self, cargo_weight,fuel_c, km, fuel, *parts):
        self._cargo_weight = cargo_weight

        super().init(fuel_c, km, fuel, *parts)




    def calculate_fuel(self):
        super().calculate_fuel()

        i = 1
        if self._cargo_weight >= 1:
            self._fuel_consumption = (self._cargo_weight // 1) * 0.1 + self._fuel_consumption
        return self._fuel_consumption # О це от +10 %

        t=10   # Перевірка Ваги
        if self._cargo_weight>t:
            print("Максимум 10т ваги")
        elif self._cargo_weight == t:
            print("Вага вантажівки рівно 10 т")
        elif self._cargo_weight<t:
            print("Вага вантажівки в нормі")


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

    t1 = Truck(1, 1, 2000, 10000, body, roof, wheel1, wheel2, wheel1part, wheel2part, window1, window2)
    #t1.show()
    t1.Go()
    t1.PrintData()
    mainloop()