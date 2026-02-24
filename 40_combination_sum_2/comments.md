**Solution Runtime:** `123ms` (Beats `5.12%`)
**Solution Memory:** `21.62mb` (Beats `12.73%`)



**Thoughts**

I'm not happy with this solution, and will probably revisit it in the future.
But I'm super limited on time today so this is what I got. 

The biggest annoyance in this problem was dealing with the list aliasing, mostly 
when memo-izing. I eventually gave in and just used deep copies. But I highly
doubt that's the best option here.

