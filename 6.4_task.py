class Car:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = None

    def go(self):
        print(f'Автомобиль {self.color} {self.name} начал движение')

    def stop(self):
        print(f'Автомобиль {self.color} {self.name} остановился')

    def turn(self, direction):
        print(f'Автомобиль {self.color} {self.name} повернул {direction}')

    def show_speed(self):

        if self.speed > 0:
            print(f'Автомобиль {self.color} {self.name} движется со скоростью {self.speed} км/ч')
            if not self.is_police:
                if self.speed > self.speed_limit:
                    print('Нарушение скоростного режима, необходимо снизить скорость')
        else:
            print(f'Автомобиль {self.color} {self.name} стоит на месте')


class TownCar(Car):
    speed_limit = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False


class SportCar(TownCar):
    speed_limit = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False


class WorkCar(Car):
    speed_limit = 40

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


porsche_911 = SportCar(60, 'зелёный', 'Порше 911')
porsche_911.stop()
porsche_911.show_speed()

vw_golf = TownCar(70, 'серый', 'Фольксваген Гольф')
vw_golf.go()
vw_golf.turn('на восток')
vw_golf.show_speed()

lada_vesta = PoliceCar(90, 'белая', 'полицейская Лада Веста')
lada_vesta.go()
lada_vesta.turn('на юго-запад')
lada_vesta.show_speed()

kamaz_45143 = WorkCar(50, 'оражевый', 'самосвал КамАЗ')
kamaz_45143.go()
kamaz_45143.turn('в сторону улицы Ленина')
kamaz_45143.show_speed()

toyota_mark2 = SportCar(0, 'серебристая', 'Тойота Марк 2')
toyota_mark2.show_speed()
