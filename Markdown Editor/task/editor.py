print("$ python markdown-editor.py")
formats = ['plain', 'bold', 'italic', 'link', 'inline-code', 'header', 'ordered-list', 'unordered-list', 'line-break']
while 1:
    choice = input("- Choose a formatter: ")
    if choice == "!help":
        print("""Available formatters: plain bold italic link inline-code header ordered-list unordered-list line-break
Special commands: !help !done""")
    elif choice in formats:
        pass
    elif choice == "!done":
        break
    else:
        print("Unknown formatting type or command. Please try again")
