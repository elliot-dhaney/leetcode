**META**

Difficulty - Medium

**Problem Statement**

You are given a positive integer `days` representing the total number of days an employee is available for work (starting from day `1`). You are also given a `2D` array `meetings` of size `n` where, `meetings[i] = [start_i, end_i]` represents the starting and ending days of meeting `i` (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

Note: The meetings may overlap.

 

Example 1:

```
Input: days = 10, meetings = [[5,7],[1,3],[9,10]]
Output: 2
```

Example 2:

```
Input: days = 5, meetings = [[2,4],[1,3]]
Output: 1
```

Example 3:

```
Input: days = 6, meetings = [[1,6]]
Output: 0
``` 

Constraints:

```
1 <= days <= 109
1 <= meetings.length <= 105
meetings[i].length == 2
1 <= meetings[i][0] <= meetings[i][1] <= days
```