# print("Добрий день")
import random

class Dog:

    def __init__(self, name):
        self.name = name
        self.energy = 50
        self.progress = 0
        self.alive = True

    def to_train(self):
        print('Time to train!')
        self.progress += 0.10
        self.energy -= 3

    def to_sleep(self):
        print('Time to sleep...')
        self.energy += 2

    def to_chill(self):
        print('Rest time...')
        self.progress -= 0.1
        self.energy += 4

    def is_alive(self):
        if self.energy <= 0:
            print('So sad dog(')
            self.alive = False
        elif self.progress < -0.5:
            print('Your human so angry!')
            self.alive = False
        elif self.progress > 5:
            print('You are good boy/girl!')
            self.alive = False

    def end_of_day(self):
        print(f'Gladness - {self.energy}')
        print(f'Progress - {self.progress}')

    def live(self, day):
        day = f'Day {day} of {self.name} life'
        print(f'{day:=^50}')
        cube = random.randint(1, 3)
        if cube == 1:
            self.to_train()
        elif cube == 2:
            self.to_sleep()
        elif cube == 3:
            self.to_chill()

        self.end_of_day()
        self.is_alive()

deive = Dog(name='You')
for day in range(1,4015):
    if not deive.alive:
        break
    deive.live(day)