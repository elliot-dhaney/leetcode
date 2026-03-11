**META**

Difficulty - Easy

**Problem Statement**

There is a hidden integer array `arr` that consists of `n` non-negative integers.

It was encoded into another integer array `encoded` of length `n - 1`, such that `encoded[i] = arr[i] XOR arr[i + 1]`.

You are given the encoded array. You are also given an integer `first`, that is the first element of `arr`, i.e. `arr[0]`.

Return the original array `arr`.

 
Example 1:

```
Input: encoded = [1,2,3], first = 1
Output: [1,0,2,1]
```

Example 2:

```
Input: encoded = [6,2,7,3], first = 4
Output: [4,2,0,7,4]
``` 

Constraints:

```
2 <= n <= 104
encoded.length == n - 1
0 <= encoded[i] <= 105
0 <= first <= 105
```