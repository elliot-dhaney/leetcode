class Solution:
    def longestString(self, x, y, z):
        # The key is the constraint:
        # 'This new string must not contain "AAA" or "BBB" as a substring.'
        # This provides limitations on what transitions we can have.
        # Let X = 'AA', Y = 'BB', Z = 'AB'. Then:
        # X -> Y
        # Z -> XY or Z
        # Y -> XY or Z
        # We always can use all of the Zs, and swapping more than once between Y 
        # and Z doesn't give any benefit. So we want to get the longest string 
        # from the Xs and Ys, which depends on which one we have more of 
        # (XYXY...XYX or YXYXY...XY, respectively).

        if (y == x):
            return 2 * z + 4 * y         # Z...ZXYXY...XY
        elif (y < x):
            return 2 * z + 4 * y + 2     # Z...ZXYXY...XYX
        elif (y > x):
            return 2 + 4 * x + 2 * z     # YXYXY...XYZ...Z
            
    def solve(self, inputs):
        return self.longestString(inputs['x'], inputs['y'], inputs['z'])
        