#2022-leetcode issues
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

            if m * n != len(original):
                return []
            result =[]
            temp =0
            for _ in range(m):
                row = original[temp:temp+n]
                result.append(row)
                temp+=n
            return result
#1954-leetcode issues
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        def ok(p):
            center = p*(p+1)
            base = center + (p*2+1)
            last = base + (p*2+1) * (p-1)
            total = (base+last) * p + center
            return total >= neededApples
        l, r = 1, int(1e5)
        while l <= r:
            mid = (l + r) // 2
            if ok(mid):
                r = mid - 1
            else:
                l = mid + 1
        return 4*2*l
#1935-leetcode issues
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        s = text.split()
        c = 0
        for i in s:
            if all(l not in brokenLetters for l in i):
                c += 1
        return c

