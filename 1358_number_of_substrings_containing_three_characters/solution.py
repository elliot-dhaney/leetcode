class Solution:
    def numberOfSubstrings(self, s):
        # Growing window from 0-3 to 0-k where s[0:k] is the first substring with 
        # all 3 characters. There are len(s)-k such substrings. Then bring window 
        # down to 3 character width from the left and try again.

        substringCount = 0
        sLength = len(s)

        i = 0
        j = 0
        characterCount = { 'a': 0, 'b': 0, 'c': 0 }
        while (i < sLength-2 and j < sLength):
            # Extend the window until it contains all 3 characters.
            while (j < sLength):
                characterCount[s[j]] += 1
                if (self.doesContainAllCharacters(characterCount)):
                    substringCount += sLength - j
                    j += 1
                    break
                j += 1

            # Remove the first character from our window + count.
            while (i <= j-2):
                characterCount[s[i]] -= 1
                i += 1
                if (not self.doesContainAllCharacters(characterCount)):
                    break

                # If we still have all the characters, add these substrings
                substringCount += sLength - j + 1

        return substringCount

    def doesContainAllCharacters(self, characterCount):
        return (
            characterCount['a'] > 0 and 
            characterCount['b'] > 0 and 
            characterCount['c'] > 0
        )



    def solve(self, inputs):
        return self.numberOfSubstrings(inputs['s'])
