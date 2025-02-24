n = int(input("Enter number of lines: "))
Tcount = 0
Scount = 0
for _ in range(n):
    lines = input()
    print(lines)
    for char in lines:
        char = char.lower()
        
        Tcount += char.count('t')
        Scount += char.count('s')
        print(Tcount, Scount)
if Tcount > Scount:
    print("English")
else:
    print("French")