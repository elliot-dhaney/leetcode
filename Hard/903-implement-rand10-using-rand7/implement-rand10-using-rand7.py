# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            # Uniform between 1-49
            val = (rand7() - 1) * 7 + rand7()
            if (val <= 40):
                return (val % 10) + 1
        
