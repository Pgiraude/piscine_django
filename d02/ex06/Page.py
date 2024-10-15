from elem import Elem, Text
from elements import Html, Head, Body, H1, Title, H2, Div, Table, Ul, Ol, Span, Text, Li, Th, Td, P, Span, Tr

class Page():
    def __init__(self, to_verify: Elem):
        self.to_verify = to_verify

    def __str__(self):
        return str(self.to_verify)

    class ParseError(Exception):
        def __init__(self):
            super().__init__("Error parsing.")

    def rules(to_check):
        tab = [content for content in to_check.content]
        if isinstance(to_check, Html):
            if len(tab) != 2: return False
            if not isinstance(tab[0], Head): return False
            if not isinstance(tab[1], Body): return False
        if isinstance(to_check, Head):
            if len(tab) != 1 or not isinstance(tab[0], Title): return False
        if isinstance(to_check, Body) or isinstance(to_check, Div):
            for elem in tab:
                if not (isinstance(elem, H1) or isinstance(elem, H2) or isinstance(elem, Div)
                or isinstance(elem, Table) or isinstance(elem, Ul) or isinstance(elem, Ol)
                or isinstance(elem, Span) or isinstance(elem, Text)): return False
        if (isinstance(to_check, Title) or isinstance(to_check, H1) or isinstance(to_check, H2)
        or isinstance(to_check, Li) or isinstance(to_check, Th) or isinstance(to_check, Td)):
            if len(tab) == 1 and not isinstance(tab[0], Text): return False
            if len(tab) > 1: return False
        if isinstance(to_check, P):
            if len(tab) > 0:
                for elem in tab:
                    if not isinstance(elem, Text): return False
        if isinstance(to_check, Span):
            if len(tab) > 0:
                if isinstance(tab[0], Text): 
                    for elem in tab:
                        if not isinstance(elem, Text): return False
                elif isinstance(tab[0], P): 
                    for elem in tab:
                        if not isinstance(elem, P): return False
                else: return False
        if isinstance(to_check, Ul) or isinstance(to_check, Ol):
            if len(tab) > 0:
                for elem in tab:
                    if not isinstance(elem, Li): return False
        if isinstance(to_check, Tr):
            if len(tab) == 0: return False
            if isinstance(tab[0], Th): 
                for elem in tab:
                    if not isinstance(elem, Th): return False
            elif isinstance(tab[0], Td): 
                for elem in tab:
                    if not isinstance(elem, Td): return False
            else: return False
        if isinstance(to_check, Table):
            if len(tab) == 0: return False
            for elem in tab:
                if not isinstance(elem, Tr): return False
        return True

    def recursive_check(to_check):

        if not Page.rules(to_check):
            return False
        tab = [content for content in to_check.content]
        for elem in tab:
            if not Page.recursive_check(elem):
                return False
        print('Rules is Ok!')
        return True
         

    def is_valid(self):
        if Page.recursive_check(self.to_verify):
            print("YES!!!")
            return True
        else:

            print(":(")
        return False

        


def write_to_file():
    readline

def test():
    test = Page(Html([Head([Title()]), Body([H1()])]))
    test.is_valid()
    print(test)


if __name__ == '__main__':
    test()