from data import dataset

def addAuto(car, race, points):

    if car in dataset:
        if race in dataset[car]:
            dataset[car][race] += " "+points
        else:
            dataset[car][race]=[points]
    else:
        dataset[car]={race:[points]}

if __name__ == "__main__":
    while True:
        addUserAuto(input("Enter a car: "),input("Enter a race :"),input("Enter a points: "))
        print(dataset)