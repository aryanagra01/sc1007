from typing import List

class Solution:
    def activity_selection(self, start_times: List[int], end_times: List[int]) -> List[int]:

       #storing the index 0,1,2, .. n-1
       activities = list(range(len(start_times)))
       activites.sort(key = lambda i: end_times[i])

       selected = []
       last_end_time = -1

       for i in activities:
            if start_time[i] >= last_end_time:
                selected.append(i)
                last_end_time = end_times[i]
        
        return selected
        




if __name__ == "__main__":
    print("Activity Selection Program")
    print("==========================")
    while True:
        starts = input("\nEnter the start times separated by spaces (blank line to quit): ").split()
        if not starts:
            break
        ends = input("Enter the end times separated by spaces: ").split()
        try:
            start_times = [int(s) for s in starts]
            end_times = [int(e) for e in ends]
        except ValueError:
            print("Invalid input! Please enter integers only.")
            continue
        if len(start_times) != len(end_times):
            print("There must be the same number of start and end times.")
            continue

        print("\nEvent  Start  End")
        for i in range(len(start_times)):
            print(f"{i:>5}  {start_times[i]:>5}  {end_times[i]:>3}")

        selected = Solution().activity_selection(start_times, end_times)
        print("\nSelected events:", selected)
        if selected is not None:
            print("Number of events scheduled:", len(selected))
