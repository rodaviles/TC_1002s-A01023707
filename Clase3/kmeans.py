#Algoritmo K-means

import numpy as np

def distance(a,b):

    a=np.array(a)**2
    b=np.array(b)**2
    return np.sqrt(a+b)

def close (puntos,centros):
    closest=[]
    clusters=[ [] for f in centros]

    for i, punto in enumerate(puntos):
        this_distance=[]
        for j,centro in enumerate(centros):
            this_distance.append(distance(punto,centro))
        this_argmin=np.arg_min(this_distance)
        closest.append(this_argmin)
        clusters[this_argmin].append(punto)

    return clusters, closest

def centers(clusters):

    for cluster in clusters:
        sum=0
        for i in range(len(cluster)):
            sum+= cluster[i]
