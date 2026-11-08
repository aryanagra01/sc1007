from typing import List

class Solution:
    def find_median_sorted_arrays(self, num1: List[int], num2: List[int]) -> float:
        
        #asssign 2 new names for ease, and get totoal, which can be even or odd (reuqiring diff median calcualtion)
        A, B = num1, num2
        total = len(num1) + len(num2)
        half = (total + 1) // 2 #plus one to ensure left always has the one extra if odd, and if even then no diff

        #ensure A is the shorter one
        if len(B) < len(A):
            A, B = B, A 
        
        # Search all possible partition positions in num1 (0 to m)
        low, high = 0, len(A)

        # Include equality to check the last remaining partition.
        # If invalid, the boundaries cross and the loop ends.
        while low <= high:
            #get the point of partition for A
            i = (low + high) // 2
            j = half - i  #number of left side of B, left will have one more if odd, but not necessarily j

            #get the elements on the edges
            #lefts if dont exist then negative infiintu, if none on fight than positive infinity
            Aleft = A[i - 1] if i > 0 else float('-inf')   #i - 1 becaseu index is 1 less than the number transferred
            Aright = A[i] if (i) < len(A) else float('inf')
            Bleft = B[j - 1] if j > 0 else float('-inf')
            Bright = B[j] if (j) < len(B) else float('inf')

            #partitiion is correct, all left elements <= right elements
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1: #if odd total
                    return max(Aleft, Bleft) #return the ighest of the left ones
                
                #else if even, get the highest of left and lowest of right and avg it
                return (max(Aleft, Bleft) + min(Aright, Bright))/ 2
            
            #else if the partition is not vlaid

            #Aleft bigger means he partition on the top has to move left towards smaller numbers
            elif Aleft > Bright:

                #ignore all the right side of the array and set the high as below the partition we just did
                high = i - 1

            #both problems cant coexist at the same time so this is wen Bleft is bigger, means partition moves righ    
            else:

                #set the low to the current partittion and one higher
                #we -1 and +1 becaeu we know that he current i is wrong alreadyso exclude it and we dont want to get stuck in a loop
                low = i + 1


if __name__ == "__main__":
    print("Median of Two Sorted Arrays Program")
    print("===================================")
    while True:
        first = input("\nEnter the first sorted array separated by spaces (q to quit): ").strip()
        if first.lower() == "q":
            break
        second = input("Enter the second sorted array separated by spaces: ").strip()
        try:
            num1 = [int(v) for v in first.split()]
            num2 = [int(v) for v in second.split()]
        except ValueError:
            print("Invalid input! Please enter integers only.")
            continue
        if not num1 and not num2:
            print("At least one array must be non-empty.")
            continue
        if num1 != sorted(num1) or num2 != sorted(num2):
            print("Both arrays must be sorted in ascending order.")
            continue

        print("Median:", Solution().find_median_sorted_arrays(num1, num2))
