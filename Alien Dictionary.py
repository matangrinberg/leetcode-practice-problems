from collections import OrderedDict
import numpy as np

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

         ############################
        ## Step 0: Pre-processing
        ############################
        outputString = ""
        num_of_words = len(words)
        allLetters = []
        for w in words:
            for letter in w:
                if letter not in allLetters:
                    allLetters.append(letter)

        num_of_letters = len(allLetters)


        ############################
        ## Step 1: Extract dependency rules (i.e. a before b)
        ############################

        ruleList = []

        # Ordering from first letters
        firstLettersDups, firstLetters = [w[0] for w in words], []
        prevLetter = None


        for currLetter in firstLettersDups:
            if currLetter not in firstLetters:
                firstLetters.append(currLetter)
                if prevLetter:
                    ruleList.append([prevLetter, currLetter])
                prevLetter = currLetter

            elif prevLetter != currLetter :
                indices = [i for i, x in enumerate(firstLettersDups) if x == currLetter]
                numDups = len(indices)
                if (indices[-1] - indices[0]) + 1 >= numDups:
                    print('Flag 1, invalid initial lettering.')
                    return ""

        # Ordering from within words

        for i in range(0, num_of_words - 1):
            currentWord, nextWord = words[i], words[i + 1]
            minLen = min(len(currentWord), len(nextWord))
            indexOfDifference = next((i for i in range(minLen) if currentWord[i]!=nextWord[i]), None)

            if nextWord in currentWord[0:int(minLen)] and nextWord != currentWord:
                print('Flag 2, prefix in subsequent word.')
                return ""

            if indexOfDifference:
                edge = [currentWord[indexOfDifference], nextWord[indexOfDifference]]
                ruleList.append(edge)

        ############################
        ## Step 2: Turn dependency rules into a graph with letters as nodes and dependencies as edges
        ############################

        adjacencyList = [[] for i in range(num_of_letters)]
        indegreeList = np.zeros(num_of_letters)
        for rule in ruleList:
            node1, node2 = rule[0], rule[1]
            node1index = allLetters.index(node1)
            node2index = allLetters.index(node2)
            adjacencyList[node1index].append(node2)
            indegreeList[node2index] += 1

        #############################
        ## Step 3: Topologically sort the graph nodes
        #############################

        zeroIndices = np.where(indegreeList == 0)[0]
        queue = map(allLetters.__getitem__, zeroIndices)

        while queue:
            # adding next letter from queue into the word
            letter = queue.pop()
            outputString += letter

            # finding where letter leads to
            letterIndex = allLetters.index(letter)
            letterTails = adjacencyList[letterIndex]

            # exploring tails
            for tail in letterTails:
                # decrementing tail indegree
                tailIndex = allLetters.index(tail)
                indegreeList[tailIndex] += -1

                if indegreeList[tailIndex] == 0:
                    if (tail in queue) or (tail in outputString):
                        return ""

                    else:
                        queue.append(tail)

        if len(allLetters) != len(outputString):
            return ""

        return(outputString)

        
