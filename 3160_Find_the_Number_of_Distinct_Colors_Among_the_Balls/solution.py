class Solution:
    def queryResults(self, limit, queries):
        # Simple solution

        ballColors = {}
        colorUses = {}
        uniqueColors = 0
        result = []
        for query in queries:
            ball = query[0]
            color = query[1]
            if (ball in ballColors):
                # Ignore if we set the ball to the same color
                if (ballColors[ball] == color):
                    result.append(uniqueColors)
                    continue

                # Lower the count for the old ball color.
                oldColor = ballColors[ball]
                colorUses[oldColor] = max(0, colorUses[oldColor] - 1)
                if (colorUses[oldColor] <= 0):
                    uniqueColors -= 1
      
            # Update the count for the new color
            if (color in colorUses and colorUses[color] > 0):
                colorUses[color] += 1
            else:
                colorUses[color] = 1
                uniqueColors += 1

            ballColors[ball] = color
            result.append(uniqueColors)

        return result

    def solve(self, inputs):
        return self.queryResults(inputs['limit'], inputs['queries'])
