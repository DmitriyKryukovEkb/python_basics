import time


class TrafficLight:

    def __init__(self, name, color):
        self.__color = color
        self.colors = ('красным', 'желтым', 'зеленым')
        self.delays = (7, 2, 5)
        self.name = name

    def running(self):
        for i, color_1, in enumerate(self.colors):
            self.__color = color_1
            print(f'Светофор {self.name} горит {self.__color}')
            time.sleep(self.delays[i])

 
tlight_lenina_st = TrafficLight('на Ленина', 'зеленым')
tlight_lenina_st.running()
