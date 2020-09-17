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
        for i in range(len(cluster)):
            sum+= cluster[i]
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


print(list_x)
print(list_y)

print("The distance is {}".format(distancia(list_x,list_y)))
print("They are {} close".format(close(list_x,list_y)))
print("The centers in x are {}".format(centers(list_x)))
print("The centers in y are {}".format(centers(list_y)))
