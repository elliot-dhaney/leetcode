class Solution:
    def interpret(self, command: str) -> str:
        index = 0
        parsed = ''
        while (index < len(command)):
            if (command[index] == "G"):
                parsed += "G"
                index += 1
            elif (command[index+1] == ')'):
                parsed += "o"
                index += 2
            else:
                parsed += "al"
                index += 4
        return parsed