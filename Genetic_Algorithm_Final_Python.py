import numpy as np, random, operator, pandas as pd
#Importing necessary libraries

class CityMap:
    def __init__(self): #Constructor of the function, sets the initial values for the data
        self.vertices = {} #Points on the map
        self.edges = {} #Lines between the points on the map
        #self.vertex_data = {}
        #self.edge_data = {}
        self.traffic_lights = set()

    def add_vertex(self, vertex, location=None): #Function to add a point to the map
        self.vertices[vertex] = location #Add the specified location to the specified point within 'vertices' (as a dictionary entry)

    def remove_vertex(self, vertex): #Function to remove a point from the map
        del self.vertices[vertex] #Remove the specified vertex from 'vertices'
        self.edges = {k: v for k, v in self.edges.items() if vertex not in k} #Remove any edges connected to the vertex

    def add_edge(self, start_vertex, end_vertex, weight, additional_info=None): #Function to add edges between vertexes
        if start_vertex not in self.vertices or end_vertex not in self.vertices: #Check if specified edge's vertices exist already
            raise ValueError("Start or end vertex does not exist in the map.")
        self.edges[(start_vertex, end_vertex)] = {'weight': weight, 'info': additional_info} #For the start and end point tuple's location, add weight and other informational dictionary (as a dictionary entry-->I.e. x={(1,2):{weight:2,info:info}})

    def remove_edge(self, start_vertex, end_vertex): #Function to remove edges between vertexes
        del self.edges[(start_vertex, end_vertex)]

    def get_vertices(self): #Returns the keys for the vertices (practically a list of all the vertices, without their locations)
        return list(self.vertices.keys())

    def get_edges(self): #Returns the keys for the edges (practically a list of all the connections between the vertices, without their weight or info)
        return list(self.edges.keys())

    def get_vertex_location(self, vertex): #Returns the location of a specific vertex
        return self.vertices[vertex]

    def add_traffic_light(self, vertex): #Adds traffic lights to the specified vertex
        self.traffic_lights.add(vertex)

    def remove_traffic_light(self, vertex): #Removes traffic lights from the specified vertex
        self.traffic_lights.discard(vertex)

    def has_traffic_light(self, vertex): #Returns a boolean which tells whether the specified vertex has a traffic light or not
        return vertex in self.traffic_lights

    def get_edge_weight(self, start_vertex, end_vertex): #Returns the weight of a specific edge
        return self.edges[(start_vertex, end_vertex)]['weight']

    def get_edge_info(self, start_vertex, end_vertex): #Returns the information of a specific edge
        return self.edges[(start_vertex, end_vertex)]['info']

    def get_neighbors(self, vertex): #Function that returns the neighbors of a specific edge
        neighbors = []
        for (start_vertex, end_vertex) in self.edges.keys():
            if start_vertex == vertex:
                neighbors.append(end_vertex)
        return neighbors

map1=CityMap() #Create a variable to be modified by the commands

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

class City: #Class which handles cities and distance calculations (currently the distance is calculated using the pythagorian theorem only, it does not account for weight)
    def __init__(self, x, y): #x and y coordinate for a city (vertex)
        self.x = x
        self.y = y
    
    def distance(self, city): #distance function, which calculates the distance betweeen two points
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance
        #edge weight is not accounted for, as the map code does not make it possible to read vertex indexes from locations, meaning this whole section would have to be rewritten

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")" #reformats the x and y coordinates as a set of strings
    
cityList = [] #default list of cities (vertices) the code uses
citySelection=random.sample(map1.get_vertices(), k=8) #k amount of cities are randomly selected from our map (this represents the route selection, so, if needed, it can be just overwritten with any set of vertices)

for i in range(len(citySelection)): #for every vertex inside our sample
    xyvalues=map1.get_vertex_location(citySelection[i]) #extract the x and y values as a dictionary
    cityList.append(City(x=xyvalues['x'], y=xyvalues['y'])) #substitute our x and y values into the original City code (note: the original code just randomly choose these values, which is what is replaced with our predetirmened values)

class Fitness: #Fitness class which calculates the fitness of each route (inverse of distance)
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness= 0.0

    def routeDistance(self, map): #Function which calculates the distance of a specific route
        if self.distance == 0:
            pathDistance = 0
            for i in range(0, len(self.route)): #for the length of the route
                fromCity = self.route[i] #set the starting city
                toCity = None 
                if i + 1 < len(self.route): #set the ending city to the next value if fromCity is not the endPoint
                    toCity = self.route[i + 1]
                else:
                    toCity = self.route[0] #setting the value in the bracket to zero means that the truck has to return to the original position
                pathDistance += fromCity.distance(toCity) #cummulative distance calculation for the route
            self.distance = pathDistance
        return self.distance #returns the cummulative distance between all the vertices
    
    def routeFitness(self): #Function which creates the actual fitness value, using the inverse of the distance
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance(map1))
        return self.fitness

def createRoute(cityList): # This function creates a random route from the cityList (though the input is already randomized in this example, it is needed as it is used to create further populations later on as well)
    route = random.sample(cityList, len(cityList))
    return route #Note: in this code, an individual corresponds to a route, i.e. a route is an individual

def initialPopulation(popSize, cityList): #Function which creates a population (route) set of a specific size
    population = []

    for i in range(0, popSize):
        population.append(createRoute(cityList)) #adds a random route as many times as specified
    return population

def rankRoutes(population): #Ranks and orders the routes based on fitness
    fitnessResults = {}
    for i in range(0,len(population)): #for as long as the population input is
        fitnessResults[i] = Fitness(population[i]).routeFitness() #calculate the fitness for the current population (route)
    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True) #once finished, order the results into a list

def selection(popRanked, eliteSize): #Parent selection based on fitness proportionate selection (fitness of each individual is checked and selected relative to the whole population)
    selectionResults = []
    df = pd.DataFrame(np.array(popRanked), columns=["Index","Fitness"]) #creates a special type of array which makes it easier to handle the data within
    df['cum_sum'] = df.Fitness.cumsum() #gives the cumulative sum of elements in an axis and writes it into the dataframe (array)
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum() #percentage relative to the cummulative sum (total population)?
    #Not entirely sure, but this is likely the part which compares the individual fitness to the overall fitness
    
    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0]) #grabs the best performing individuals from the ranked list (grabs the best one as many times as specified by eliteSize)
    for i in range(0, len(popRanked) - eliteSize): #for the remaining individuals
        pick = 100*random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i,3]:
                selectionResults.append(popRanked[i][0]) #if within threshehold, add a random individual to the selection as well
                break
    return selectionResults

def matingPool(population, selectionResults): #Function which extracts the selected individuals from the population and creates a common matingpool
    matingpool = []
    for i in range(0, len(selectionResults)): #for as many as were selected
        index = selectionResults[i] 
        matingpool.append(population[index]) #add the selected individual from the original population to the matingpool
    return matingpool

def breed(parent1, parent2): #Function which breeds two parents using ordered crossover (random subset is choosen from one parent and the rest is filled by the other parent's genes)
    child = []
    childP1 = []
    childP2 = []
    
    geneA = int(random.random() * len(parent1)) #create a gene from parent 1
    geneB = int(random.random() * len(parent1)) #create another gene from parent 1
    
    startGene = min(geneA, geneB) #represents the starting point from which the gene will be extracted from?
    endGene = max(geneA, geneB) #represents the end of the gene section we will be extracting from parent 1?

    for i in range(startGene, endGene):
        childP1.append(parent1[i]) #extracts the genetic code snipet from parent 1 and applies it to the child
        
    childP2 = [item for item in parent2 if item not in childP1] #substitute remaining parts of gene from parent 2

    child = childP1 + childP2 #combine snipet and reamining parts
    return child

def breedPopulation(matingpool, eliteSize): #Generalized breeding code, able to breed a whole population
    children = []
    length = len(matingpool) - eliteSize 
    pool = random.sample(matingpool, len(matingpool)) #mix the matingpool

    for i in range(0,eliteSize):
        children.append(matingpool[i]) #using elitism, starts filling the children pool with the best individuals
    
    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool)-i-1]) #breed children
        children.append(child) #fill remaining places within children
    return children

def mutate(individual, mutationRate): #Mutation function, which uses swap mutation (giving a low probability to two cities swapping places)
    for swapped in range(len(individual)): #for the length of the route (remember, an individual is represented as a route in this case)
        if(random.random() < mutationRate): #if the random 'event' says to mutate
            swapWith = int(random.random() * len(individual)) #tells which city to swap with?
            
            city1 = individual[swapped] #the current, to be swapped vertex
            city2 = individual[swapWith] #the vertex which will be swaped
            
            individual[swapped] = city2
            individual[swapWith] = city1 #Swaps the cities
    return individual

def mutatePopulation(population, mutationRate): #Mutate function which is ran through the whole population
    mutatedPop = []
    
    for ind in range(0, len(population)): #runs the mutation code for the whole population
        mutatedInd = mutate(population[ind], mutationRate) #mutates the current individual (route) with the specified mutation rate
        mutatedPop.append(mutatedInd)
    return mutatedPop

def nextGeneration(currentGen, eliteSize, mutationRate): #Function which generates a new generation when it is called
    popRanked = rankRoutes(currentGen) #runs the route ranking and sorting
    selectionResults = selection(popRanked, eliteSize) #selects the best performing individuals
    matingpool = matingPool(currentGen, selectionResults) #creates a matingpool using the best individuals
    children = breedPopulation(matingpool, eliteSize) #breeds/creates a new set of population based on the previous generations best genes
    nextGeneration = mutatePopulation(children, mutationRate) #mutates the new generation
    return nextGeneration


def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations): #Final assembly of the previous codes, it creates an initial population to start with and then creates new generations as many times as specified
    pop = initialPopulation(popSize, population) #creating the initial population (popSize is how many routes it will create, population is the set of cities (vertices))
    print("Initial distance: " + str(1 / rankRoutes(pop)[0][1])) #shows the initial distance for debugging
    
    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate) #creates new generations the specified amount of times
    
    print("Final distance: " + str(1 / rankRoutes(pop)[0][1])) #Shows the final distance
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex] #conserves the best route
    print('\n')
    print("Final route:",'\n')
    print(bestRoute)
    print('\n')
    return bestRoute #printable best route

geneticAlgorithm(population=cityList, popSize=100, eliteSize=20, mutationRate=0.01, generations=500) #Final function that can be called to carry out the genetic algorithm

print("Initial vertex set:",'\n')
print(cityList)