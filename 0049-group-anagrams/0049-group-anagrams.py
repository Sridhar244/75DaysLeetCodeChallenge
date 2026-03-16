class Solution(object):
    def groupAnagrams(self, strs):
        res={}
        for i in strs:
            key=''.join(sorted(i))
            if key not in res:
                res[key]=[i]
            else:
                res[key].append(i)
        return res.values()


            
        