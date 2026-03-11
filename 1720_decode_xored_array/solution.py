class Solution:
    def decode(self, encoded, first):
        arr = [first]
        for val in encoded:
            arr.append(val ^ first)
            first = val ^ first
        return arr

    def solve(self, inputs):
        return self.decode(inputs['encoded'], inputs['first'])
