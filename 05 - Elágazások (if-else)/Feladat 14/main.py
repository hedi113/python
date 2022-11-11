x: int = None
y: int = None
z: int = None

print("Kérem az x értékét: ", end="")
x = int(input())

print("Kérem az y értékét:", end="")
y = int(input())

print("Kérem a z értékét: ", end="")
z = int(input())

if (x % y == 0 and x % z == 0):
    print("A szám osztható y-nal és x-szel is.")
elif x % z == 0:
    print("Az x osztható z-vel.")
elif (x % y == 0):
    print("Az x osztható y-nal.")
else: 
    print("Az x egyik számmal sem osztható.")