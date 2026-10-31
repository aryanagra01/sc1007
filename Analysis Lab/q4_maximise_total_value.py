import itertools

class Solution:
    def brute_force_knapsack(self, weights, values, W):
        n = len(weights)
        best_value = 0
        best_items = []
        best_weight = 0

        for i in range(2 ** n):                 # one number per subset
            items = []
            total_weight = 0
            total_value = 0
            for j in range(n):
                if (i >> j) & 1:                # bit j is on: take item j
                    items.append(j)
                    total_weight += weights[j]
                    total_value += values[j]
            if total_weight <= W and total_value > best_value:
                best_value = total_value
                best_items = items
                best_weight = total_weight

        return [best_value, best_items, best_weight]

    def knapsack_2(self, weights, values, W):
        best_value = 0
        best_items = []
        best_weight = 0

        for r in range(len(weights) + 1):          # try every subset size, including 0
            for combo in itertools.combinations(range(len(weights)), r):
                total_weight = sum(weights[i] for i in combo)
                if total_weight <= W:               # too heavy: skip it
                    total_value = sum(values[i] for i in combo)
                    if total_value > best_value:    # keep the most valuable legal set
                        best_value = total_value
                        best_items = list(combo)
                        best_weight = total_weight

        return [best_value, best_items, best_weight]


    def brute_force_knapsack_3(self, weights, values, W):
        n = len(weights)
        best_value = 0
        best_items = []

        def helper(i, chosen, total_weight, total_value):
            nonlocal best_value, best_items
            if i == n:                              # no artifacts left to decide
                if total_value > best_value:
                    best_value = total_value
                    best_items = chosen.copy()      # save a copy before pop() clears chosen
                return
            helper(i + 1, chosen, total_weight, total_value)   # skip item i
            if total_weight + weights[i] <= W:                 # take item i only if it fits
                chosen.append(i)
                helper(i + 1, chosen, total_weight + weights[i], total_value + values[i])
                chosen.pop()

        helper(0, [], 0, 0)
        selected_items = []
        total_selected_weight = 0
        for i in best_items:
            selected_items.append([weights[i], values[i]])
            total_selected_weight += weights[i]
        return [best_value, selected_items, total_selected_weight]



if __name__ == "__main__":
    print("Brute-Force Knapsack Program")
    print("============================")
    while True:
        capacity = input("\nEnter the backpack capacity W (blank line to quit): ").strip()
        if not capacity:
            break
        try:
            W = int(capacity)
            values = [int(v) for v in input("Enter the values separated by spaces: ").split()]
            weights = [int(w) for w in input("Enter the weights separated by spaces: ").split()]
        except ValueError:
            print("Invalid input! Please enter integers only.")
            continue
        if len(values) != len(weights):
            print("There must be the same number of values and weights.")
            continue

        print("\nArtifact  Weight  Value")
        for i in range(len(values)):
            print(f"{i:>8}  {weights[i]:>6}  {values[i]:>5}")

        print("\n[max value, selected items, total weight] =", Solution().brute_force_knapsack(weights, values, W))
