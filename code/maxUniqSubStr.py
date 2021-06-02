"""
Twitter-OA
Consider a given string, minLen and maxLen as well as uniqMax.
Find substring whose length is in between minLen and maxLen.
Return the maximum number of unique substring <= uniqMax.

Example 1:
Input: components='abcde', minLen=2, maxLen=3, uniqMax=4
Output: 1 
Explanation: All substrings are unique, thus return 1
    substrings=['ab', 'bc', 'cd', 'de', 'abc', bcd', 'cde']

Example 2:
Input: components='abababc', minLen=2, maxLen=3, uniqMax=4
Output: 3 
Explanation: 'ab' is repeated 3 times, thus return 3    
    substrings=['ab', 'ba', 'ab', 'ba', 'ab', 'bc', 'aba', 'bab', 'aba', 'bab', 'abc']
    # ab         1           2           3
    # ba               1           2                
    # aba                                            1             2 
    # bab                                                   1             2 
"""
class Solution:
    def maxUniqSubString(self, components, minLen, maxLen):
        uniqD = dict()     
        n = len(components)
        for i in range(n-maxLen+1):
            for j in range(i+minLen, i+maxLen+1):    
                #print(components[i:j])
                if components[i:j] not in uniqD:
                    uniqD[components[i:j]] = 1
                else:
                    uniqD[components[i:j]] += 1
        return max(uniqD.values())

s = Solution()
components, minLen, maxLen, uniqMax ='abcde', 2, 3, 4
components, minLen, maxLen, uniqMax ='abababc', 2, 3, 4
print(s.maxUniqSubString(components, minLen, maxLen))

