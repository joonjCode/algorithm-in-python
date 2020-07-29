class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp = {}
        ans = []
        for word in strs:
            sortedword = ''.join(sorted(word))
            
            if sortedword not in tmp:
                tmp[sortedword] = [word]
            else:
                tmp[sortedword].append(word)
        
        for _,v in tmp.items():
            ans.append(v)
            
        return ans

