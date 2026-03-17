x=int(input("DIGITE UM VALOR DE 0 A 99: "))
y=int(input("DIGITE OUTRO VALOR DE 0 A 99: "))

nmax=max(x,y)
nmin=min(x,y)

while(nmin<nmax):
    print(nmin)
    nmin=nmin+1
