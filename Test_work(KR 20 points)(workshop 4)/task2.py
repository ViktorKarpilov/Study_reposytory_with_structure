from data import dataset
#    Створити пакет validators та написати функції, що валідують усі дані. Імпорутвати дані функції.
from validators.lib import getCar
from validators.lib import getCompetition
from validators.lib import getResults
from task1 import addAuto


#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник.
#   Усі дані вводить користувач. Використати валідатори. Викликати функцію
def addUserAutoValidator():

    Corect = False
    while not Corect:
        car = getCar()
        if car:
            Corect = True

    Corect = False
    while not Corect:
        competition = getCompetition()
        if competition:
            Corect = True

    Corect = False
    while not Corect:
        points = getResults()
        if points:
            Corect = True

    addAuto(car, competition, points)

addUserAutoValidator()
print(dataset)
