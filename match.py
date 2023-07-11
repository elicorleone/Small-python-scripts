name = input("What's your name? ")

match name:
    case "Eli" | "Pedro" | "Bandido":
        print("Family")
    case "Viki":
        print("Cousin")
    case _:
        print("Who?")
