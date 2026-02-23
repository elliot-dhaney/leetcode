**Solution Runtime:** `47ms` (Beats `76.78%`)
**Solution Memory:** `51.43mb` (Beats `69.35%`)


**Thoughts**

This problem seemed like an Easy one to me. I had a solution in mind immediately,
and the only hurdle I initially had to consider was solved by the constraint
that the keys can't contain parenthesis characters.

The use of a dictionary for the knowledge seemed like an obvious one, assuming
memory usage for it wasn't a major concern and we could get some performance out
of starting each index search after the previous found pair. 