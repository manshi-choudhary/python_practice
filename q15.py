with open("file.exe","r") as f:
    i="twinkle"
    c=f.read()
    if i in c:
        print("yes its have the word twinkle!!")
    else:
        print("no it doesn't have twinkle")
