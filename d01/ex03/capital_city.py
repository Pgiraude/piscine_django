import sys

def capital_city(state: str):

    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }

    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }

    if state in states:
        print(capital_cities[states[state]])
    else:
        print("Unknown state")
        

def main():
    if len(sys.argv) == 2:
        capital_city(sys.argv[1])
    
if __name__ == '__main__':
    main()