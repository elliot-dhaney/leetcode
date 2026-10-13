class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        index = 0
        counts = [0, 0]

        while (index < len(s)):
            # Get the index at the start of the next contiguous segment.
            nextIndex = s.find(
                self.getAltZeroOrOne(s[index]), 
                index
            )

            # Update the counts, given the current segment.
            if (nextIndex == -1):
                counts[int(s[index])] = max(
                    counts[int(s[index])],
                    len(s) - index
                )
                break
            counts[int(s[index])] = max(
                counts[int(s[index])],
                nextIndex - index
            )

            # Update the index to the start of the next contiguous segment.
            index = nextIndex

        return counts[1] > counts[0]

    def getAltZeroOrOne(self, c: str) -> str:
        # Returns '1' when c is '0' and '0' when c is '1'.
        return str((int(c) + 1) % 2)
