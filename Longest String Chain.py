# We will start at the longest word and work backwards
# We can use a map where each KEY is a word ending, each VALUE is the LENGTH of the longest possible word sequence ending with this word. This is MEMOIZATION. It avoids recalcuation.

class Solution(object):
    def __init__(self):
        self.memo = defaultdict(list)

    def DFS(self, wordsPresent, currentWord):
        if self.memo.has_key(currentWord):
            return self.memo[currentWord][0]
        maxLength = 1

        for i in range (0, len(currentWord)):
            newWord = currentWord[:i] + currentWord[(i+1):]
            if newWord in wordsPresent:
                currentLength = 1 + self.DFS(wordsPresent, newWord)
                maxLength = max(maxLength, currentLength)
        self.memo[currentWord].append(maxLength)
        return maxLength

    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        wordsPresent = set()
        wordsPresent.update(words)
        count = 0
        for word in words:
            count = max(count, self.DFS(wordsPresent, word))
        return count
        
