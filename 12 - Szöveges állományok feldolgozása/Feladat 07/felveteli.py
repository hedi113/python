magyarJegy: int = 0
matekJegy: int = 0

print("Adja meg a magyar nyelv jegyet: ", end="")
magyarJegy = int(input())
print("Adja meg a matematika jegyet: ", end="")
matekJegy = int(input())

if((magyarJegy > 5 or magyarJegy < 1) and (matekJegy > 5 or matekJegy < 1)):
    print("A magyar nyelv és matematika jegy érvénytelen!")
elif(magyarJegy > 5 or magyarJegy < 1):
    print("A magyar nyelv jegy érvénytelen!")
elif(matekJegy > 5 or matekJegy < 1):
    print("A matematika jegy érvénytelen!")

