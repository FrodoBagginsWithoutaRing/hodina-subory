slov={'item1':45.50,'item2':35,'item3':41.30,'item4':5,'item5':24}
#zotriedit a napisat prve 3 ---> du


#1. bez sorted -> utriedim si ho sam, vypisem prve tri bubllesoort/vyberom, najdes maximum vypises a odstranis atd az kym neostane nic
#2. hladame maximalny prvok v slovniku

for j in range(3):
    index_max= list(slov.keys())[0]
    moje_max=slov[index_max]

    for prvok in slov:
        if slov[prvok]>moje_max:
            moje_max=slov[prvok]
            index_max= prvok
    print(moje_max,index_max)
    temp=slov.pop(index_max)

