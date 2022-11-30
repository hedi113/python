month: str = None

month = input("Milyen hónap van?")

match month:
    case "január":
        print("1.")
    case "február":
        print("2.")
    case "március":
        print("3.")
    case "április":
        print("4.")
    case "május":
        print("5.")
    case "június":
        print("6.")
    case "július":
        print("7.")
    case "augusztus":
        print("8.")
    case "szeptember":
        print("9.")
    case "október":
        print("10.")
    case "november":
        print("11.")
    case "december":
        print("12.")
    case _:
        print("Ilyen hónap nincs.")