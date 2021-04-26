import heapq, math

# Return the 2 nearest locations

# get the distance for each location
# return locations based on 2 shortest ones

def nearest_n_locations(allLocations: list,numLocations: int) -> list:
    distance_each_location = []
    if len(allLocations) == 0 and len(allLocations) > numLocations:
        return distance_each_location

    heapq.heapify(distance_each_location)

    for locations in allLocations:
        sol = pow(locations[0],2) + pow(locations[1],2)
        distance = math.sqrt(sol)
        heapq.heappush(distance_each_location,[distance,locations])

    nearest = [heapq.heappop(distance_each_location)[1] for x in range(0,numLocations) ]
    return nearest




allLocations = [[1,2],[3,4],[1,-1]]
numLocations = 2
nearest = nearest_n_locations(allLocations,numLocations)

print(nearest)
