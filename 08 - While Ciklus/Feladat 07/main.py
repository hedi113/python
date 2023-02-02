smaller: int = None
larger: int = 0

print("Adja meg az első számot: ", end="")
smaller = int(input())

while(smaller > larger):
    print("Adja meg a második számot (az előzőnél legyen nagyobb): ", end="")
    larger = int(input())

for i in range(smaller, larger, -1):
    print(i)
