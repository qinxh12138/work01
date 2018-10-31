class Vehicles:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def run(self):
        print(f'车子的牌子是:{self.brand}')
        print(f'车子的颜色是:{self.color}')
        print('我已开动了')

class Car(Vehicles):
    seats=4
    def __init__(self,brand,color):
        super().__init__(brand,color)
        self.run()
    @classmethod
    def show_car(cls):
        print(f'此小汽车载量{cls.seats}人')
class Truck(Vehicles):
    load=8.6
    def __init__(self,brand, color):
        super().__init__(brand, color)
        self.run()
    @classmethod
    def show_truck(cls):
        print(f'此卡车载重{cls.load}吨')

c1=Car('奔驰','黄色')
t1=Car('解放','军绿色')