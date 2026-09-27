class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            s_count = [0] * 26
            for char in s:
                s_count[ord(char) - ord('a')] += 1
            res[tuple(s_count)].append(s)
        return list(res.values())

            