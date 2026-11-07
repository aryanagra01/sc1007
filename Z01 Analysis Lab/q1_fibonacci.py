class Solution:
    def __init__(self):
        self.saveDict = {}

    def fibonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n in self.saveDict:
            return self.saveDict[n]
        else:
            value = self.fibonacci(n-1) + self.fibonacci(n-2)
            self.saveDict[n] = value
            return value
        
    def fiboannciBottomUp (self, n : int) -> int:
        digit01 = 0
        digit02 = 1
        count = 0

        for _ in range(n):
            fibSum = digit01 + digit02
            digit01 = digit02
            digit02 = fibSum
        return digit01
        
    def fibonaiccibuttomUpAns(self, n):
        if n <= 1:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range (2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def fibDP(self, n):
        def fibMemory(n, dp):
            if n <= 1:
                return n
            if dp[n] != -1:
                return dp[n]
            else:
                dp[n] = fibMemory(n-1, dp) + fibMemory(n-2, dp)
                return dp[n]
        dp = [-1] * (n+1)
        return fibMemory(n, dp)

if __name__ == "__main__":
    print("Fibonacci with Dynamic Programming")
    print("==================================")
    while True:
        try:
            value = input("\nEnter n (-1 to quit): ")
            if not value:
                continue
            n = int(value)
            if n == -1:
                break
            if n < 0:
                print("n must be a non-negative integer.")
                continue
            print(f"fibonacci({n}) = {Solution().fibonacci(n)}")
        except ValueError:
            print("Invalid input! Please enter an integer.")
