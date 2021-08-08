class Road:
    def __init__(self, length, width, name):
        self._length = length
        self._width = width
        self._name = name

    def asphalt_mass(self, unit_mass, depth):
        print(f'Масса асфальта для дороги {self._name} '
              f'составляет {self._length * self._width * unit_mass * depth / 1000:.2f} т')


lenina_st_road = Road(5000, 20, 'на улице Ленина')
lenina_st_road.asphalt_mass(25, 5)
