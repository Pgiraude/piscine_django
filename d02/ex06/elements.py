from elem import Elem, Text

def create_custom_html_class(name_tag, is_double = True):
    class CustomHtmlClass(Elem):
        def  __init__(self, content=None, attr={}):
            super().__init__(tag=name_tag.lower(), attr=attr, content=content, tag_type='double')
            if is_double is False:
                self.tag_type = 'simple'
    CustomHtmlClass.__name__ = name_tag
    return CustomHtmlClass

Html = create_custom_html_class('Html')
Head = create_custom_html_class('Head')
Body = create_custom_html_class('Body')
Title = create_custom_html_class('Title')
Meta = create_custom_html_class('Meta', False)
Img = create_custom_html_class('Img', False)
Table = create_custom_html_class('Table')
Th = create_custom_html_class('Th')
Tr = create_custom_html_class('Tr')
Td = create_custom_html_class('Td')
Ul = create_custom_html_class('Ul')
Ol = create_custom_html_class('Ol')
Li = create_custom_html_class('Li')
H1 = create_custom_html_class('H1')
H2 = create_custom_html_class('H2')
P = create_custom_html_class('P')
Div = create_custom_html_class('Div')
Span = create_custom_html_class('Span')
Hr = create_custom_html_class('Hr')
Br = create_custom_html_class('Br')



def test():
    test = Html([Head(), Body()])
    print(test)

if __name__ == '__main__':
    test()