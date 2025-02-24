n = int(input("Enter number of lines: "))
Tcount = 0
Scount = 0
for _ in range(n):
    lines = input()
    for char in lines:
        char = char.lower()
        Tcount += char.count('t')
        Scount += char.count('s')
if Tcount > Scount:
    print("English")
else:
    print("French")
