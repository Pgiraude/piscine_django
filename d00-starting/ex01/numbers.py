def number():
    with open("./numbers.txt", "r") as file:
        content = file.read()
        value= ""
        for char in content:
            if char.isnumeric():
                value += char
            elif len(value):
                print(value)
                value = ""

if __name__ == '__main__':
    number()