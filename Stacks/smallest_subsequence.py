#1081

class Solution:
    def smallestSubsequence(self, s: str) -> str:

        last_pos = {ch: i for i, ch in enumerate(s)}

        res = []
        seen = set()

        for i, ch in enumerate(s):
            if ch not in seen:
                while res and res[-1] > ch and last_pos[res[-1]] > i:
                    seen.remove(res.pop())

                seen.add(ch)
                res.append(ch)
        
        return ''.join(res)
        