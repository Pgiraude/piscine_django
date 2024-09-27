import os
import sys
import re
import settings

def create_html_file(html: str):
    with open("index.html", 'w') as file:
        file.write(html)

def render(file):
    if not os.path.exists(file):
        print(f"Error: The file '{file}' does not exist.")
        return
    try:
        with open(file, 'r') as template_content:
            html_content = template_content.read()
    except IOError as e:
        print(f"Error: Could not open the file '{file}'. Reason: {e}")
        return
    html = html_content.format(name=settings.name, surname=settings.surname, title=settings.title, job=settings.job, age=settings.age)
    create_html_file(html)

def main():
    if len(sys.argv) != 2:
        print("Error: Wrong number of argument")
        return
    file = sys.argv[1]
    file_name, file_extension = os.path.splitext(file)
    if file_extension != ".template":
        print(f"Error: Unsupported file extension: {file_extension}")
        return
    render(file)

if __name__ == '__main__':
    main()
