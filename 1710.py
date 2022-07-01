class Solution:
    def maximumUnits(self, boxTypes, truckSize) -> int:
        # sort boxTypes by second element
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        total = 0

        for i in boxTypes:
            if i[0] > truckSize:
                total += truckSize*i[1]
                break
            else:
                truckSize -= i[0]
                total += i[1]*i[0]
        
        return total
        

# input example: [[5,10],[2,5],[4,7],[3,9]]
list = input()
# parse input
list = list.strip('[]').split('],[')
list = [i.split(',') for i in list]
list = [[int(i) for i in j] for j in list]

truckSize = int(input())
print(Solution().maximumUnits(list, truckSize))