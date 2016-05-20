"""
Developed by Zachary Robinson

"""
import math
import random
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
import numpy
from matplotlib import cm

def hill_climb(function_to_optimize, step_size, xmin, xmax, ymin, ymax):
    current_x = 0.0
    current_y = 0.0
    current_best = function_to_optimize(current_x, current_y)
    while True:
        check = 0
        if not current_x + step_size > xmax:
            temp = function_to_optimize(current_x + step_size, current_y)
            if temp < current_best :
                current_best = temp
                current_x += step_size
                check = 1
        if not current_x - step_size < xmin:
            temp = function_to_optimize(current_x - step_size, current_y)
            if temp < current_best:
                current_best = temp
                current_x -= step_size
                check = 1
        if not current_y + step_size > ymax:
            temp = function_to_optimize(current_x, current_y + step_size)
            if temp < current_best:
                current_best = temp
                current_y += step_size
                check = 1
        if not current_y - step_size < ymin:
            temp = function_to_optimize(current_x, current_y - step_size)
            if temp < current_best:
                current_best = temp
                current_y -= step_size
                check = 1
        if not check == 1:
            return [current_x, current_y, current_best]
    

def hill_climb_random_restart(function_to_optimize, step_size, num_restarts, xmin, xmax, ymin, ymax):
    minima = []
    for i in range(0, num_restarts):
        current_x = random.uniform(xmin, xmax)
        current_y = random.uniform(ymin, ymax)
        current_best = function_to_optimize(current_x, current_y)
        
        while True:
            check = 0
            if not current_x + step_size > xmax:
                temp = function_to_optimize(current_x + step_size, current_y)
                if temp < current_best :
                    current_best = temp
                    current_x += step_size
                    check = 1
            if not current_x - step_size < xmin:
                temp = function_to_optimize(current_x - step_size, current_y)
                if temp < current_best:
                    current_best = temp
                    current_x -= step_size
                    check = 1
            if not current_y + step_size > ymax:
                temp = function_to_optimize(current_x, current_y + step_size)
                if temp < current_best:
                    current_best = temp
                    current_y += step_size
                    check = 1
            if not current_y - step_size < ymin:
                temp = function_to_optimize(current_x, current_y - step_size)
                if temp < current_best:
                    current_best = temp
                    current_y -= step_size
                    check = 1
            if not check == 1:
                minima.append([current_x, current_y, current_best])
                break
    best_minimum = minima.pop()
    
    for i in minima:
        temp = minima.pop()
        if temp[2] < best_minimum[2]:
            best_minimum = temp
            
    return best_minimum
    
#This process is plotted point by point and executes slowly.
def simulated_annealing(function_to_optimize, step_size, max_temp, xmin, xmax, ymin, ymax):
    temp = max_temp
    current_x = random.uniform(xmin, xmax)
    current_y = random.uniform(ymin, ymax)
    current_best = function_to_optimize(current_x, current_y)
    best_coords = [current_x, current_y, current_best]
    
    fig = plot.figure()
    ax = fig.add_subplot(111, projection='3d')
    xs = []
    ys = []
    zs = []
    
    while temp > .001:
        i = 0
        while i < 1000:
            xs.append(current_x)
            ys.append(current_y)
            zs.append(current_best)
            
            new_x = current_x + random.uniform(-step_size, step_size)
            new_y = current_y + random.uniform(-step_size, step_size)
            while not xmin <= new_x <= xmax:
                new_x = current_x + random.uniform(-step_size, step_size)
            while not ymin <= new_y <= ymax:
                new_y = current_y + random.uniform(-step_size, step_size)
            new_value = function_to_optimize(new_x, new_y)
            prob = math.e ** ((current_best - new_value) / temp)
            if prob > random.random():
                current_best = new_value
                current_x = new_x
                current_y = new_y
                best_coords = [current_x, current_y, current_best]
            i += 1
        temp *= .9
    ax.scatter(xs, ys, zs)
    plot.show()
    return best_coords

def simulated_annealing_climb(function_to_optimize, step_size_1, step_size_2, max_temp, xmin, xmax, ymin, ymax):
    temp = max_temp
    current_x = random.uniform(xmin, xmax)
    current_y = random.uniform(ymin, ymax)
    current_best = function_to_optimize(current_x, current_y)
    best_coords = [current_x, current_y, current_best]
    while temp > .001:
        i = 0
        while i < 1000:
            new_x = current_x + random.uniform(-step_size_1, step_size_1)
            new_y = current_y + random.uniform(-step_size_1, step_size_1)
            while not xmin <= new_x <= xmax:
                new_x = current_x + random.uniform(-step_size_1, step_size_1)
            while not ymin <= new_y <= ymax:
                new_y = current_y + random.uniform(-step_size_1, step_size_1)
            new_value = function_to_optimize(new_x, new_y)
            prob = math.e ** ((current_best - new_value) / temp)
            if prob > random.random():
                current_best = new_value
                current_x = new_x
                current_y = new_y
                best_coords = [current_x, current_y, current_best]
            i += 1
        temp *= .9
       
    while True:
        check = 0
        if not current_x + step_size_2 > xmax:
            temp = function_to_optimize(current_x + step_size_2, current_y)
            if temp < current_best :
                current_best = temp
                current_x += step_size_2
                check = 1
        if not current_x - step_size_2 < xmin:
            temp = function_to_optimize(current_x - step_size_2, current_y)
            if temp < current_best:
                current_best = temp
                current_x -= step_size_2
                check = 1
        if not current_y + step_size_2 > ymax:
            temp = function_to_optimize(current_x, current_y + step_size_2)
            if temp < current_best:
                current_best = temp
                current_y += step_size_2
                check = 1
        if not current_y - step_size_2 < ymin:
            temp = function_to_optimize(current_x, current_y - step_size_2)
            if temp < current_best:
                current_best = temp
                current_y -= step_size_2
                check = 1
        if not check == 1:
            best_coords = [current_x, current_y, current_best]
            return best_coords
    
def some_function(x, y):
    r = math.sqrt((x ** 2) + (y ** 2))
    r2 = r ** 2
    z1 = math.sin(x ** 2 + 3 * (y ** 2)) / (0.1 + r2)
    z2 = ((x ** 2) + (5 * (y ** 2)))
    z3 = math.exp(1 - r2) / 2
    z = z1 + (z2 * z3)
    return z
    
print ("Hill Climb:")  
print (hill_climb(some_function, 0.0001, -2.5, 2.5, -2.5, 2.5))
print ("Hill Climb with Restarts:")
print (hill_climb_random_restart(some_function, 0.0001, 10, -2.5, 2.5, -2.5, 2.5))
print ("Simulated Annealing:")
print (simulated_annealing(some_function, 0.01, 100, -2.5, 2.5, -2.5, 2.5))
print ("Simulated Annealing with Hill Climb:")
print (simulated_annealing_climb(some_function, 0.01, 0.0001, 100, -2.5, 2.5, -2.5, 2.5))


#plotting for the function
x = numpy.arange(-2.5, 2.5, .01)
y = numpy.arange(-2.5, 2.5, .01)
x, y = numpy.meshgrid(x, y)
r = numpy.sqrt((x ** 2) + (y ** 2))
r2 = r ** 2
z1 = numpy.sin(x ** 2 + 3 * (y ** 2)) / (0.1 + r2)
z2 = ((x ** 2) + (5 * (y ** 2)))
z3 = numpy.exp(1 - r2) / 2
z = z1 + (z2 * z3)


fig = plot.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plot.show()

