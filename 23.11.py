#stringi v nom novy zoznam obsahuje pocty samohlasok v jednot string
mena=['jozo','pato','karol','akoze','neviem','uz','co','pisat','preto','dusan ma mamu']
samohlasky='euioay'
zoz=[]
p=0

for i in range(len(mena)):
    for a in range(len(mena[i])):
        kontrola=mena[i]
        if kontrola[a] in samohlasky:
            p=p+1
        else:
            p=p
    zoz.append(p)
    p=0

print(zoz)
