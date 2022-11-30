valasztas: int = None

print("Válasszon üdítőt:\n1 - Coca Cola\n2 - Pepsi\n3 - Fanta\n4 - Sprite")
valasztas = int(input())

match valasztas: 
    case 1:
        print("Az ön által választott üdítő: Coca Cola.")
    case 2:
        print("Az ön által választott üdítő: Pepsi.")
    case 3:
        print("Az ön által választott üdítő: Fanta.")
    case 4:
        print("Az ön által választott üdítő: Sprite.")
    case _:
        print("Az ön által választott üdítő nem szerepel a kínálatban.")
