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
        else:
            print("Unknown formatting type or command. Please try again")
            continue
        print(markdown)


if __name__ == '__main__':
    main()
