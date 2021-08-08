class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} пишет')


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} рисует')


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} выделяет')


pen = Pen('Ручка')
pen.draw()
pencil = Pencil('Карандаш')
pencil.draw()
handle = Handle('Маркер')
handle.draw()
