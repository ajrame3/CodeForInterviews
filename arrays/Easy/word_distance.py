class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        word1_index = -1
        word2_index = -1

        dist = len(wordsDict)

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                word1_index = i
            elif wordsDict[i] == word2:
                word2_index = i
            
            if word1_index != -1 and word2_index != -1:
                dist = min(dist, abs(word2_index - word1_index))
        
        return dist