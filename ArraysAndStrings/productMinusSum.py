class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sSum=0
        pSum=1
        for i in str(n):
            pSum*=int(i)
            sSum+=int(i)
        return pSum-sSum

        