from beverages import HotBeverage, Coffee, Tea, Chocolate,Cappuccino
import random

class CoffeeMachine:
    def __init__(self):
        self.served_count = 0
        self.isWorking = True

    class EmptyCup(HotBeverage):
        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90

        def description(self):
            return "An empty cup?! Gimme my money back!"
    
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")


    def repair(self):
        self.served_count = 0
        self.isWorking = True

    def serve(self, some_beverage):
        if not self.isWorking or self.served_count >= 10:
            self.isWorking = False
            raise CoffeeMachine.BrokenMachineException()

        self.served_count += 1
        if random.randrange(0, 2, 1):
            return self.EmptyCup()
        return some_beverage()



def main():
    test = CoffeeMachine()
    try:
        print(test.serve(Coffee))
        print(test.serve(Tea))
        print(test.serve(Coffee))
        print(test.serve(Cappuccino))
        print(test.serve(Chocolate))
        print(test.serve(HotBeverage))
        print(test.serve(Coffee))
        print(test.serve(Coffee))
        print(test.serve(Coffee))
        print(test.serve(Coffee))
        print(test.serve(Coffee))
    except CoffeeMachine.BrokenMachineException as e:
        print(e)

    test.repair()

    try:
        print(test.serve(HotBeverage))
    except CoffeeMachine.BrokenMachineException as e:
        print(e)


if __name__ == '__main__':
    main()