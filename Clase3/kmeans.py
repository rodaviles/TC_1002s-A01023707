#Algoritmo K-means

import numpy as np

def distancia(x,y):

    x=np.array(x)**2
    y=np.array(y)**2
    return np.sqrt(x+y)

def close (puntos,centros):
    closest=[]
    clusters=[ [] for f in centros]

    for i, punto in enumerate(puntos):
        esta_distancia=[]
        for j,centro in enumerate(centros):
            esta_distancia.append(distancia(punto,centro))
        this_argmin=np.argmin(esta_distancia)
        closest.append(this_argmin)
        clusters[this_argmin].append(punto)

    return clusters, closest

def centers(clusters):

    for cluster in clusters:
        sum=0
        for clusters in range(len(cluster)):
            sum= sum+cluster[clusters]
list_x = []
list_y = []
num = int(input("Please input the size of the lists \n"))
c1=0

while c1<num:
    x= int(input("Input x value \n"))
    y= int(input("Input y value \n"))
    list_x.append(x)
    list_y.append(y)
    c1=c1+1


print("The list looks like this\n{}".format(list_x))
print(list_y)

print("\nThe distance list is \n{}".format(distancia(list_x,list_y)))
print("\nThey closeness list is \n{}".format(close(list_x,list_y)))
list_x=str(list_x)
list_y=str(list_y)
print("\nThe centers in x list is \n{}".format(centers(list_x)))
print("\nThe centers in y list is \n{}".format(centers(list_y)))
