import numpy as np
class Solution(object):

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        output, wordsToAdd, lineCharacters = [], [], 0

        for currentWord in words:
            currentWordLength = len(currentWord)
            currentLineLength = lineCharacters + len(wordsToAdd) - 1

            # stop after current word, start creating the line
            if currentLineLength + 1 + currentWordLength > maxWidth:

                # construct Line from wordsToAdd
                line = ""
                num_in_line = len(wordsToAdd)
                spaces = maxWidth - lineCharacters
                if num_in_line == 1:
                    line += wordsToAdd[0] + " " * spaces

                else:
                    leftoverSpace = spaces % (num_in_line - 1)
                    standardSpace = " " * int(np.floor(spaces / (num_in_line - 1)))

                    for i in range(0, num_in_line - 1):
                        line += wordsToAdd[i] + standardSpace
                        if leftoverSpace > 0:
                            line += " "
                            leftoverSpace += -1

                    line += wordsToAdd[-1]

                output.append(line)
                wordsToAdd, lineCharacters = [], 0


            wordsToAdd.append(currentWord)
            lineCharacters += currentWordLength

        finalLine = " ".join(wordsToAdd).ljust(maxWidth)
        output.append(finalLine)

        return output
