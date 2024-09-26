import sys

def get_key(val: str, lst: {str: str} ):
    for key, value in lst.items():
        if val.lower() == value.lower():
            return key
    return ""

def get_value(val: str, lst: {str: str} ):
    for key, value in lst.items():
        if val.lower() == key.lower():
            return value
    return ""

def print_message(val: str):

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

    val_is_capital = get_key(val, capital_cities)
    val_is_state = get_value(val, states)

    if val_is_capital or val_is_state:
        tag = val_is_capital if val_is_capital else val_is_state
        print(capital_cities[tag], " is the capital of ", get_key(tag, states))
    else:
        print(val, " is neither a capital city nor a state")
        
def parser(input: str):
    split_input = input.split(",")
    if not len(split_input[0]):
        del split_input[0]
    values = []
    for value in split_input:
        if not len(value):
            return []
        if value.strip():
            values.append(value.strip())
    return values

def all_in(input: str):
    lst = parser(input)
    if not lst:
        return
    for val in lst:
        print_message(val)

def main():
    if len(sys.argv) == 2:
        all_in(sys.argv[1])
    
if __name__ == '__main__':
    main()