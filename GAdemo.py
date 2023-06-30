import random
import CityMap as cm
import GeneticAlgorithm as ga
#Importing necessary libraries

map1=cm.CityMap() #Create a variable to be modified by the commands

map1.add_vertex('A', {'x': 5, 'y': 10})
map1.add_vertex('B', {'x': 20, 'y': 5})
map1.add_vertex('C', {'x': 50, 'y': 5})
map1.add_vertex('D', {'x': 60, 'y':25})
map1.add_vertex('E', {'x': 65, 'y':30})
map1.add_vertex('F', {'x': 80, 'y':30})
map1.add_vertex('G', {'x': 100, 'y':40})
map1.add_vertex('H', {'x': 135, 'y':100})
map1.add_vertex('I', {'x': 150, 'y':250})
map1.add_vertex('K', {'x': 180, 'y':250})
map1.add_vertex('L', {'x': 200, 'y':200})
map1.add_vertex('M', {'x': 250, 'y':250})
#Adding vertices to the map, with a unique identifier and location

vertices=map1.get_vertices() 
for i in range(len(vertices)):
    for o in range(len(vertices)): # Two loops are used, one for the first value, the second for the other respectively
            map1.add_edge(str(vertices[i]),str(vertices[o]),random.randint(5,100)) #Adds all the vertices to the current "main" vertex
    map1.remove_edge(str(vertices[i]),str(vertices[i])) #The second for loop ads duplicates, which this code removes before moving to the next iteration
#Adding edges (connections) between the vertices, by setting the starting and ending locations and the weight of the roads

cityList = [] #default list of cities (vertices) the code uses
citySelection=random.sample(map1.get_vertices(), k=8) #k amount of cities are randomly selected from our map (this represents the route selection, so, if needed, it can be just overwritten with any set of vertices)

for i in range(len(citySelection)): #for every vertex inside our sample
    xyvalues=map1.get_vertex_location(citySelection[i]) #extract the x and y values as a dictionary
    cityList.append(ga.City(x=xyvalues['x'], y=xyvalues['y'])) #substitute our x and y values into the original City code (note: the original code just randomly choose these values, which is what is replaced with our predetirmened values)

ga.map1 = map1
ga.geneticAlgorithm(population=cityList, popSize=100, eliteSize=20, mutationRate=0.01, generations=500) #Final function that can be called to carry out the genetic algorithm

print("Initial vertex set:",'\n')
print(cityList)