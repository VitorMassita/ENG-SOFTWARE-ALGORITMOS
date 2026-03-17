xmax=-1000
ymax=-1000
count=0
while count<=10:
    y=-4*count**2 + 40*count
    if (y>ymax):
        ymax=y
        xmax=count
    count=count+1
    print(f"{count:0.1f}, {y:0.1f}")
print(f"O MAIOR DE Y PARA X E DE: {ymax:0.1f}")