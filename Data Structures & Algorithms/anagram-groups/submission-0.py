class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        resultmap={}
        for word in strs:
            sorted_word=''.join(sorted(word))
            if sorted_word not in resultmap:
                resultmap[sorted_word]=[]
            resultmap[sorted_word].append(word)
        return list(resultmap.values())       