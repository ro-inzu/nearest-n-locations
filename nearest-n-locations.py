import heapq, math

# Return the 2 nearest locations

# get the distance for each location
# return locations based on 2 shortest ones

def nearest_n_locations(allLocations: list,numLocations: int) -> list:
    nearest = []
    if len(allLocations) == 0 and len(allLocations) > numLocations:
        return nearest

    heap_list = []
    heapq.heapify(heap_list)

    for locations in allLocations:
        sol = pow(locations[0],2) + pow(locations[1],2)
        distance = math.sqrt(sol)
        heapq.heappush(heap_list,[distance,locations])

    nearest = [heapq.heappop(heap_list)[1] for x in range(0,numLocations) ]
    return nearest




allLocations = [[1,2],[3,4],[1,-1]]
numLocations = 2
nearest = nearest_n_locations(allLocations,numLocations)

print(nearest)
