class Element:
    def __init__(self, name, position, number, symbol, molar_mass, nb_electron_layers):
        self.name = name
        self.position = position
        self.number = number
        self.symbol = symbol
        self.molar_mass = molar_mass
        self.nb_electron_layers = nb_electron_layers

def create_html_file(html: str):
    file = open("index.html", 'w')
    file.write(html)

def split_and_get_end_part(str: str, separator: str):
    str_split = str.split(separator)
    return str_split[-1].strip()

def parse_line(line: str):
    split_line = line.split(',')
    part1 = split_line[0].split('=')
    name = part1[0].strip()
    position = int(split_and_get_end_part(part1[1], ':'))
    number = split_and_get_end_part(split_line[1], ':')
    symbol = split_and_get_end_part(split_line[2], ':')
    molar_mass = split_and_get_end_part(split_line[3], ':')
    val = split_and_get_end_part(split_line[4], ':').split(' ')
    value = sum(int(v) for v in val)
    lst = [2, 10, 18, 36, 54, 86, 118]
    nb_electron_layers = 1
    nb_electron_layers += sum(1 for limit in lst if value > limit)
    return Element(name, position, number, symbol, molar_mass, nb_electron_layers)

def parser(file_name: str):
    file = open(file_name, "r")
    lines = file.readlines()

    result = []
    for line in lines:
        var = parse_line(line)
        result.append(var)

    return result

def generate_cell(element: Element):
    cell = f"""<td>
    <h4>{element.name}</h4>
    <ul>
        <li>No {element.number}</li>
        <li>{element.symbol}</li>
        <li>{element.molar_mass}</li>
    </ul>
</td>
"""
    return cell

def generate_row(elements: [Element]):
    result = "<tr>"
    for i in range(0, 18):
        found = False
        for item in elements:
            if item.position == i:
                result += generate_cell(item)
                found = True
                break
        if not found:
            result += "<td></td>"
    result += "</tr>"

    return result

def generate_table(elements: [Element]):

    result = ""
    for i in range(1, 8):
        elements_flt = list(filter(lambda el: el.nb_electron_layers == i, elements))
        result += generate_row(elements_flt)
    return result

def html_generator(str):
    html = f"""<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <style>
            td {{
                border: solid 1px;
                border-collapse: collapse;
            }}
        </style>
    </head>
    <body>
        <table>
            {str}
        </table>

    </body>
</html>"""
    create_html_file(html)

def main():
    lst_elements = parser("./periodic_table.txt")
    result = generate_table(lst_elements)

    html_generator(result)

if __name__ == '__main__':
    main()
