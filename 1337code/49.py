class Solution:
    def groupAnagrams(self, strs):
        result = {}
        for s in strs:
            sortedStr = ''.join(sorted(s))
            if sortedStr in result:
                result[sortedStr].append(s)
            else:
                result[sortedStr] = [s]
        #convert dict to list
        output = []
        for key in result:
            output.append(result[key])
        return output

print(Solution().groupAnagrams(input().strip('[]').replace('"', '').split(',')))