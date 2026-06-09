class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        for i in s:
            if i in countS.keys():
                countS[i]+=1
            else:
                countS[i]=1
        countT= {}
        for j in t:
            if j in countT.keys():
                countT[j]+=1
            else:
                countT[j]=1
        return countS==countT