import itertools

class Solution:
    def brute_force_tsp(self, distance_matrix):
        n = len(distance_matrix)
        locations = list(range(n)) #0,1,2,3
        min_distance = float('inf')
        best_route = None


        #O(n!) complxity --> (n-1)! orders
        for perm in itertools.permutations(locations[1:]): #beaseu always start at factory
            #reust is tuple -> convert to lis with 0
            route  = [0] + list(perm) + [0]
            total_distance = 0

            for i in range(len(route) - 1): #number of gaps is 1 less
                total_distance += distance_matrix[route[i]][route[i+1]]
            
            if total_distance < min_distance:
                min_distance = total_distance
                best_route = route

        return [min_distance, best_route]

    def brute_force_tsp(self, distance_matrix):

        #first get the lenght of the totalnumber of locatios
        n = len(distance_matrix)
        
        shortest = float('inf')
        best_route = []

        for perm in itertools.permutations(range(1, n)): #create permuations from 1 to n-1, 0 not included becaseu its always start and end
            #permutations() already generates the routes in lexicographic order, hence no equal comparirion later just lesser than

            route = [0] + list(perm) + [0] #0, ... , 0 list convets the tuple to a list
            total_distance = 0 #initialise total distance

            for i in range(len(route) - 1): #number of gaps is one less
                total_distance += distance_matrix[route[i]][route[i + 1]]
                #for each perm, get the distance between each places, i and i+1 posiions from route, and onlky 4 becaseu 4 gaps so no porblem here
            
            #no equal than becaseu lexigraphic order, which itertools.permautions handles
            if total_distance < shortest:
                shortest = total_distance
                best_route = route
        
        return [shortest, best_route]

        #this is O(n!) time compleixty because brute fourced
            

if __name__ == "__main__":
    print("Brute-Force Travelling Salesman Program")
    print("=======================================")
    while True:
        size = input("\nEnter the number of locations, including the warehouse (blank line to quit): ").strip()
        if not size:
            break
        try:
            n = int(size)
            print(f"Enter {n} rows of {n} distances, separated by spaces:")
            distance_matrix = [[int(d) for d in input(f"  row {i}: ").split()] for i in range(n)]
        except ValueError:
            print("Invalid input! Please enter integers only.")
            continue
        if any(len(row) != n for row in distance_matrix):
            print(f"Each row must have exactly {n} distances.")
            continue

        print("\n[min distance, best route] =", Solution().brute_force_tsp(distance_matrix))
