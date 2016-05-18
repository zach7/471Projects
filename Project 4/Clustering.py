# -*- coding: utf-8 -*-
"""
Created on Mon May 16 21:47:01 2016

@author: Zach
"""
import sys
import random
import math
import matplotlib.pyplot as plot

points = []
centroids = []
old_centroids = []
clusters = [None] * int(sys.argv[1])

print (sys.argv[2])

try:
    #Read in points
    inFile = open(sys.argv[2], 'r')
    for line in inFile:
        thisLine = line.split(' ')
        point = (int(thisLine[0]), int(thisLine[1]))
        points.append(point)
        
    check = False
    
    
    #generate centroids
    for i in range(0, int(sys.argv[1])):
        x = random.uniform(-1000, 1000)
        y = random.uniform(-1000, 1000)
        centroids.append((x, y))
        old_centroids.append((x, y))
        clusters[i] = []
      
    #loop through points, assigning each to a cluster and updating centroids
    #looping ends once centroids stabilized (points no longer changing clusters)      
    while not check:
        for i in clusters:
            i.clear()
        #calculate distance of point from each centroid (only square of distance needed)
        for i in points:
            _min = ((i[0] - centroids[0][0]) ** 2) + ((i[1] - centroids[0][1]) ** 2)
            cluster = 0
            for j in range(1, int(sys.argv[1])):
                dist = ((i[0] - centroids[j][0]) ** 2) + ((i[1] - centroids[j][1]) ** 2)
                if (dist < _min):
                    _min = dist
                    cluster = j
            #append point to cluster of least distance
            clusters[cluster].append(i)
        
        #for each centroid, recalculate based on new cluster
        for i in range(0, int(sys.argv[1])):
            x_sum = 0
            y_sum = 0
            for j in clusters[i]:
                x_sum += j[0]
                y_sum += j[1]
            if not len(clusters[i]) == 0:
                centroids[i] = ((x_sum / len(clusters[i])), (y_sum / len(clusters[i])))
            
        check = True
        #check to see if centroids have changed
        for i in range(0, int(sys.argv[1])):
            if not ((math.isclose(centroids[i][0], old_centroids[i][0])) and (math.isclose(centroids[i][1], old_centroids[i][1]))):
                print (centroids[i], "*")
                print (old_centroids[i])
                check = False
        if not check:
            for i in range(0, int(sys.argv[1])):
                old_centroids[i] = centroids[i]
                
#Plotting: Centroids appear as Triangles
    xs = []
    ys = []
    
    color = 0
    for i in clusters:
        for j in i:
            xs.append(j[0])
            ys.append(j[1])
        if color == 0:
            plot.plot(xs, ys, 'yo')
            plot.scatter(centroids[color][0], centroids[color][1], s = 200, color = 'y', marker = '^')
        elif color == 1:
            plot.plot(xs, ys, 'ro')
            plot.scatter(centroids[color][0], centroids[color][1], s = 200, color = 'r', marker = '^')
        elif (color % 7) == 0:
            plot.plot(xs, ys, 'bo')
            plot.scatter(centroids[color][0], centroids[color][1], s = 200, color = 'b', marker = '^')
        elif (color % 5) == 0:
            plot.plot(xs, ys, 'mo')
            plot.scatter(centroids[color][0], centroids[color][1], s = 200, color = 'm', marker = '^')
        elif (color % 3) == 0:
            plot.plot(xs, ys, 'go')
            plot.scatter(centroids[color][0], centroids[color][1], s = 200, color = 'g', marker = '^')
        elif (color % 2) == 0:
            plot.plot(xs, ys, 'ko')  
            plot.scatter(centroids[color][0], centroids[color][1], s = 200, color = 'k', marker = '^')
        color += 1
        xs.clear()
        ys.clear()
    plot.show()
except ValueError:
    print ('Error')
