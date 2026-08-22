class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            ArrS = list(s)
            ArrT = list(t)
            ArrS.sort()
            ArrT.sort()
            sortS = ArrS
            sortT = ArrT
            for i in range(len(s)):
                if sortS[i] != sortT[i]:
                    return False
            return True
        else:
            return False