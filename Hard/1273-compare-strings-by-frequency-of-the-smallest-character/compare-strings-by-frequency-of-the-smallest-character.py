class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        counts = []
        for word in words:
            counts.append(self.f(word))
        counts.sort()

        answer = []
        for query in queries:
            count = self.f(query)
            answer.append(self.binarySearch(counts, count))
        
        return answer

        
    def binarySearch(self, counts, count):
        ''' 
            Returns the number of elements bigger than count in counts
        '''
        numCounts = len(counts)
        low = 0
        high = numCounts - 1
        while (high > low):
            index = low + (high - low) // 2
            if (index == numCounts - 1):
                if (count < counts[index]):
                    return 1
                else:
                    return 0
            
            if (counts[index] <= count < counts[index + 1]):
                return numCounts - index - 1

            # Update bounds of the search
            if (count < counts[index]):
                high = index
            else:
                if (low != index):
                    low = index
                else:
                    low = high

        if (count < counts[high]):
            return numCounts - high
        return numCounts - high - 1

    def f(self, s):
        '''
            Calculates the frequency of the lexicographically smallest character in s
        '''
        # Guaranteed len(s) >= 1
        minC = s[0]
        count = 0
        for c in s:
            if c < minC:
                count = 1
                minC = c
            elif c == minC:
                count += 1
        return count