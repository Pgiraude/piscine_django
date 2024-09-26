import sys

def get_key(val: str, lst: {str: str} ):
    for key, value in lst.items():
        if val == value:
            return key
    return ""


def state(capital: str):

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

    result = get_key(capital, capital_cities)
    if result:
        print(get_key(result, states))
    else:
        print("Unknown capital city")
        

def main():
    if len(sys.argv) == 2:
        state(sys.argv[1])
    
if __name__ == '__main__':
    main()