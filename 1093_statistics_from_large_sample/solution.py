class Solution:
    def sampleStats(self, count):
        output = [-1, -1, -1, -1, -1]

        # mean vars
        totalSum = 0
        
        # median vars
        firstMedianIndex = -1
        partialCountSum = 0
        totalCountSum = sum(count)
        
        mode = [-1, -1]

        for index, num in enumerate(count):
            if (num > 0):
                if (output[0] == -1):
                    output[0] = index
                output[1] = index

                totalSum += index * num
                if (mode[1] < num):
                    mode = [index, num]

                # The median lies in the middle of an indexes' count
                if (partialCountSum < totalCountSum / 2 and partialCountSum + num > totalCountSum / 2):
                    output[3] = index
                # First half of a split median.
                elif (totalCountSum % 2 == 0 and partialCountSum + num == totalCountSum // 2):
                    firstMedianIndex = index
                # Second half of a split median
                elif (firstMedianIndex >= 0):
                    output[3] = (firstMedianIndex + index) / 2
                    firstMedianIndex = -1

                partialCountSum += num

        output[2] = totalSum / totalCountSum
        output[4] = mode[0]

        return output

    def solve(self, inputs):
        return self.sampleStats(inputs['count'])
