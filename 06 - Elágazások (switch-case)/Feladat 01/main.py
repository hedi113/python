day: int = None

day = input("Hányadik napja van a hétnek?")

match day:
    case "1":
        print("Ma hétfő van.")
    case "2":
        print("Ma kedd van.")
    case "3":
        print("Ma szerda van.")
    case "4":
        print("Ma csütörtök van.")
    case "5":
        print("Ma péntek van.")
    case "6":
        print("Ma szombat van.")
    case "7":
        print("ma vasárnap van.")
    case _:
        print("A hétnek ilyen napja nincs.")