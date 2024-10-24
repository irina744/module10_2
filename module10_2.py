from time import sleep
from threading import Thread

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f"{self.name} на нас напали!")
        self.enemy = 100
        self.days = 0
        while self.enemy > 0:
            print(f"{self.name} сражается {self.days} days..., осталось {self.enemy} воинов.")
            sleep(1)
            self.enemy -= self.power
            self.days += 1


        if self.enemy <= 0:
            print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
