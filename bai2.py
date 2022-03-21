hoten = input("nhap ho ten:  ")
hoten = hoten.title()
hoten = hoten.split()
hoten = reversed(hoten)
for x in hoten:
    print(x,end=" ")