fr=open('co kukas/udaje.txt','r',encoding="utf-8")
slovnik={}
ms=fr.read()
konriad=0
for znak in ms:
    if znak.isupper() or znak.islower():
        slovnik[znak]= slovnik.get(znak,0) +1
    if znak == "\n":
        konriad= konriad +1
print(slovnik)
print(konriad)



#aky je priemerny pocet znakov v jednom riadku?
#Koloko je tam medzier
#Bonus subor na zapisovanie kde napises tento subor odzadu
#mam subor a ako ho prechadzat:
#1. sposob:
# for riadok in fr: #riadok reprezentuje jeden riadok
#     print(riadok.strip()) #strip aby neboli medzeri

#2. sposob tzv megastring
# ms=fr.read()
# print(ms)


#3.sposob ked riadky potrebujem spracovat inak

# prvy_riadok= fr.readline() #citacia hlava - precita prvy a caka na zaciatku druheho
# print(prvy_riadok)
#
# druhy_riadok=fr.readline()
# print(druhy_riadok)
#
#
# for riadok in fr:
#     print(riadok)

 #4 sposob
# zoz_riadkov=fr.readlines()
# print(zoz_riadkov)
# acko='a'
# becko='b'
# cecko='c'
# for i in range (len(zoz_riadkov)):
#     for a in range (len(zoz_riadkov[i])):
#         kontorla=zoz_riadkov[i]
#         if kontorla[a] in a:
#             p_a=p_a+1
#         elif kontorla[a] in a:
#             p_b=p_b+1
#         elif kontorla[a] in a:
#             p_c=p_c+1
#
# print(p_a,p_b,p_c)
