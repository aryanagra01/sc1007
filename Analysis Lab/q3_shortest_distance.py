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
