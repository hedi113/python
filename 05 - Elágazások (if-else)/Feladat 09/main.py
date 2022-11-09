x: int = None
y: int = None
eredmeny: float = None

print("Kérem az x értékét: ", end="")
x = int(input())

print("Kérem az y értékét:", end="")
y = int(input())

eredmeny = x % y

if eredmeny == 0:
    print("X osztója y-nak.")
else:
    print("Az y nem osztója x-nek.")