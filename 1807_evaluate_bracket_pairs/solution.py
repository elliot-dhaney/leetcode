class Solution:
    def evaluate(self, s, knowledge):
        # Construct a dictionary of the knowledge, for quicker access.
        knowledgeDict = {}
        for pair in knowledge:
            knowledgeDict[pair[0]] = pair[1]

        index = 0
        output = ''
        while (index < len(s)):
            # knowledge keys only contain lowercase alphabet. So searching for 
            # '(' and ')' will not result in cutting keys in half.
            # (if keys could contain '(' or ')', we would have to count paren balance.)

            try:
                startIndex = s.index('(', index)
                endIndex = s.index(')', index)
            except ValueError:
                # No more keys, just copy the rest of the string.
                output += s[index:]
                break

            # The key is the substring between the found start and end indices.
            key = s[startIndex + 1: endIndex]
            if (key in knowledgeDict):
                value = knowledgeDict[key]
            else:
                value = '?'

            # Copy all of the string from our prior index to our new key parens.
            # Then insert the key's value and update index to just after the parens.
            output += s[index:startIndex] + value
            index = endIndex + 1

        return output

    def solve(self, inputs):
        return self.evaluate(inputs['s'], inputs['knowledge'])
