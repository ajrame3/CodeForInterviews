class WordDistance:

    def __init__(self, wordsDict: List[str]):

        self.words_index_dict = defaultdict(list)

        for i, word in enumerate(wordsDict):
            self.words_index_dict[word].append(i)

        

    def shortest(self, word1: str, word2: str) -> int:

        word_index1 = self.words_index_dict[word1]
        word_index2 = self.words_index_dict[word2]

        i, j, dist = 0, 0, float("inf")

        while i < len(word_index1) and j < len(word_index2):
            dist = min(dist, abs(word_index1[i] - word_index2[j]))
            if word_index1[i] < word_index2[j]:
                i += 1
            else:
                j += 1
        
        return dist
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)