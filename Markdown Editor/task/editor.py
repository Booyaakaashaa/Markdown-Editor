def header():
    level = int(input("- Level: "))
    if not 0 < level < 7:
        return 1
    text = input("- Text: ")
    return "#" * level + " " + text + "\n"


def plain():
    text = input("- Text: ")
    return text


def line_break():
    return "\n"


def bold():
    return "**" + input("- Text: ") + "**"


def italic():
    return "*" + input("- Text: ") + "*"


def inline():
    return "`" + input("- Text: ") + "`"


def link():
    return "[" + input("- Label: ") + "]" + "(" + input("- URL: ") + ")"


def md_list(order):
    rows = int(input("- Number of rows: "))
    if rows < 1:
        return 0
    out = ""
    if order == 0:
        for i in range(1, rows + 1):
            out += f"{i}." + input(f"- Row #{i}: ") + '\n'
    else:
        for i in range(1, rows + 1):
            out += "* " + input(f"- Row #{i}: ") + "\n"
    return out


def main():
    print("$ python markdown-editor.py")
    # formats = ['plain', 'bold', 'italic', 'link', 'inline-code', 'header', 'ordered-list', 'unordered-list', 'line-break']
    markdown = ""
    while 1:
        choice = input("- Choose a formatter: ")
        if choice == "!help":
            print("""Available formatters: plain bold italic link inline-code header ordered-list unordered-list line-break
    Special commands: !help !done""")
        elif choice == "!done":
            break
        elif choice == "plain":
            markdown += plain()
        elif choice == "bold":
            markdown += bold()
        elif choice == "italic":
            markdown += italic()
        elif choice == "inline-code":
            markdown += inline()
        elif choice == "link":
            markdown += link()
        elif choice == "header":
            if header == 1:
                print("The level should be within the range of 1 to 6")
                continue
            markdown += header()
        elif choice == "line-break":
            markdown += line_break()
        elif choice == "ordered-list":
            if md_list(0) == 0:
                print('The number of rows should be greater than zero')
                continue
            markdown += md_list(0)
        elif choice == "unordered-list":
            if md_list(1) == 0:
                print('The number of rows should be greater than zero')
                continue
            markdown += md_list(1)
        else:
            print("Unknown formatting type or command. Please try again")
            continue
        print(markdown)


if __name__ == '__main__':
    main()
