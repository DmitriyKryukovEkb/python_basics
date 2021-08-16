def validate(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ValueError:
            print('Недостаточно единиц на складе!')
        except KeyError:
            print('Не найдена такая позиция на складе!')
    return wrapper


class Storage:
    """
    equipment_units = {
    'equipment_type': {
    'name': {
    'model': {
    'count': ''
    }
    }
    }
    }
    """
    equipment_units = {}

    @classmethod
    @validate
    def storage_to(cls, unit_type, unit_name, unit_model, unit_count):
        cls.equipment_units[unit_type][unit_name][unit_model]['count'] += unit_count

    @classmethod
    @validate
    def storage_from(cls, unit_type, unit_name, unit_model, unit_count):
        current_count = cls.equipment_units[unit_type][unit_name][unit_model]['count']
        if current_count < unit_count:
            raise ValueError
        else:
            cls.equipment_units[unit_type][unit_name][unit_model]['count'] -= unit_count

    @staticmethod
    def get_all_equipment():
        for key, value in Storage.equipment_units.items():
            print(key, value)


class Equipment:
    def __init__(self, name, model, eq_type, count=0):
        self.name = name
        self.model = model
        self.eq_type = eq_type
        try:
            if type(count) not in [int, float]:
                self.__count = 0
                raise ValueError
        except ValueError:
            print('Неверный формат данных!')
        else:
            self.__count = count
        finally:
            self.update_storage_info()

    def update_storage_info(self):
        equipment_storage_info = Storage.equipment_units.get(self.eq_type, {})
        if self.name in equipment_storage_info.keys():
            equipment_storage_info_by_name = equipment_storage_info[self.name]
            if self.model in equipment_storage_info_by_name.keys():
                equipment_storage_info_by_model = equipment_storage_info_by_name[self.model]
                equipment_storage_info_by_model['count'] += self.__count
            else:
                equipment_storage_info_by_name[self.model] = {'count': self.__count}
        else:
            equipment_storage_info[self.name] = {self.model: {'count': self.__count}}

        Storage.equipment_units[self.eq_type] = equipment_storage_info


class Printer(Equipment):
    def __init__(self, name, model, count, colors):
        super().__init__(name, model, 'Printer', count)
        self.colors = colors


class Notebook(Equipment):
    def __init__(self, name, model, count, ram, system_type):
        super().__init__(name, model, 'Notebook', count)
        self.ram = ram
        self.system_type = system_type


my_printer_1 = Printer('HP', '1018', 30, ['black'])
my_notebook_1 = Notebook('Lenovo', 'Legion 5', 20, 16, 'DOS')

Storage.get_all_equipment()

Storage.storage_to(unit_type='Notebook', unit_name='Lenovo', unit_model='Legion 5', unit_count=5)
Storage.get_all_equipment()

Storage.storage_from(unit_type='Printer', unit_name='HP', unit_model='1018', unit_count=10)
Storage.get_all_equipment()
