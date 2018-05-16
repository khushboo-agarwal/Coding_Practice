class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[1 ^ i for i in row[::-1]] for row in A]



s = Solution()

A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

B = s.flipAndInvertImage(A)
print('A', A)

print('B', B)