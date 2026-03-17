class Solution(object):
    def topKFrequent(self, nums, k):
        freq=Counter(nums)
        return [x[0] for x in sorted(freq.items(),key=lambda x:x[1],reverse=True)[:k]]