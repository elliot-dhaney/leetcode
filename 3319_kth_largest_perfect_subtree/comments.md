**Solution Runtime:** `44ms` (Beats `32.90%`)
**Solution Memory:** `19.96mb` (Beats `98.37%`)

**Thoughts**

Fairly simple tree traversal problem, just have to keep track of all subtrees.

To improve the runtime efficiency, there's probably some small improvements but 
I doubt there's any huge strategy improvements. Maybe using that the answer was 
always going to be 2^(depth) - 1 where depth is how tall the kth largest 
perfect subtree is.
