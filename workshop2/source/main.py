"""



1.Написати рекурсивну функцію, що виводить brand авто з найбільшою кількістю
власників.
def getBrand(smth):
#some magic
return brand
2. Написати функцію, що до авто з брендом brand додає нового власника з іменем
name
def addOwner(smth, name):
#some magic
3. Написати функцію, повертає множину усых власників усіх автомобілів.
def getNames(smth):
#some magic
"""



if __name__ == "__main__":

    def getBrand(smth):
        """функція для модифікації результату Brand без декорування
           Args: smth
           Returns: String
           Example:Ford
           """
        return Brand(smth)[0]


    def Brand(smth):
        """Шукає марку із найбільшим числом власників
           Args: smth
           Returns: list
           Example:["Ford",2]
           """
        if (len(smth) > 1):
            a = Max(get(smth[0]), Brand(smth[1:]))
        else:
            return get(smth[0])
        return a


    # Brand = Returner(Brand)
    def get(car):
        """Повертає Марку і кіл-ть власників
           Args: dict
           Returns: list
           Example:["Ford",2]
           """
        return [car["brand"], len(car["owners"])]


    def Max(a, b):
        """Порывнюэ два об'єкта типу list,формату[str,int]
           Args: list ,list
           Returns: list
           Example:["Ford",2] ["Mers",1] => ["Ford",2]
           """
        if (a[1] > b[1]):
            return a
        else:
            return b


    def addOwner(smth, name):
        """Додаэ ще одного власника в сет з найбільшим числом власників
           Args: список словників , str
           Returns: None
           Example: [{'brand': 'Mers', 'model': 'C500', 'year': 2000, 'owners': {'asdasd', 'asd', 'Biba'}}] =>  {'brand': 'Mers', 'model': 'C500', 'year': 2000, 'owners': {'asdasd', 'asd', 'Biba', 'Bob'}}
           """
        name1 = {name}
        brand = getBrand(smth)
        for i in smth:
            needed = str(i['brand'])
            if needed == brand:
                i['owners'].update(name1)


    def getNames(smth):
        """Виводить імена власників марки із найбільшим числом власників
           Args: список словників
           Returns: set
           Example:
               getNames([{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'owners': {'Mark', 'Boba'}}, {'brand': 'Mers', 'model': 'C500', 'year': 2000, 'owners': {'asdasd', 'asd', 'Biba', 'Bob'}}])
               {'asdasd', 'asd', 'Biba', 'Bob', 'Mark', 'Boba'}

           """
        names = set()
        for j in smth:
            names.update(j['owners'])
        return names


    smth = [
        {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964,
            'owners': {
                "Mark",
                "Boba"
            }
        },
        {
            "brand": "Mers",
            "model": "C500",
            "year": 2000,
            'owners': {
                "Bob"
            }
        },
        {"brand": "Wolksvagen",
         "model": "Polo",
         "year": 2002,
         "owners": {}
         }
    ]
    print(getBrand(smth))
    addOwner(smth, 'Biba')
    print(smth)
    print(getNames(smth))