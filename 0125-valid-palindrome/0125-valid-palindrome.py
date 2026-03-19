class Solution(object):
    def isPalindrome(self, s):
        output=''
        for char in s:
            if char.isalnum():
                output+=char.lower()
        return output==output[::-1]

        