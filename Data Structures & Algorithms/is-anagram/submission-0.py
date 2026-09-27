class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counts = [0] * 26

        for i in s:
            s_counts[ord(i) - ord('a')] += 1

        for j in t:
            s_counts[ord(j) - ord('a')] -= 1

        return all(count == 0 for count in s_counts)
        