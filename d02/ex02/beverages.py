class HotBeverage:
    def __init__(self):
        self.price = 0.30
        self.name = "hot beverage"
    
    def __str__(self):
        var = f"name : {self.name}\n"
        var += f"price : {self.price}\n"
        var += f"description : {self.description()}"
        return var

    def description(self):
        return "Just some hot water in a cup."

class Coffee(HotBeverage):
    def __init__(self):
        self.price = 0.40
        self.name = "coffee"
    
    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    def __init__(self):
        self.name = "Tea"
        self.price = 0.30

class Chocolate(HotBeverage):
    def __init__(self):
        self.price = 0.50
        self.name = "chocolate"
    
    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    def __init__(self):
        self.price = 0.45
        self.name = "cappuccino"
    
    def description(self):
        return "Un po' di Italia nella sua tazza!"


def main():
    hot_beverage = HotBeverage()
    print(hot_beverage)

    coffee = Coffee()
    print(coffee)

    tea = Tea()
    print(tea)

    chocolate = Chocolate()
    print(chocolate)

    cappuccino = Cappuccino()
    print(cappuccino)

if __name__ == '__main__':
    main()