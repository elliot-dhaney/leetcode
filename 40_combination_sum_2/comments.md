**New Solution Runtime:** `17ms` (Beats `58.21%`)
**New Solution Memory:** `19.9mb` (Beats `12.99%`)

**New Thoughts**

I originally avoided converting the combinations to strings because it was kind 
of a pain. But it is much better. Not great, I still barely beat 50%, and memory
usage is not good. But a 8x improvement in runtime is nice.

After looking at other solutions, mine is definitely overcomplicated. But I am
a little surprised that the ones I saw are performant enough to pass the tests.
The major improvement I saw was mostly trimming "runs" of candidates. I considered 
this but not long enough to convince myself it wouldn't affect output. Which, in 
hindsight, is obvious and I should have implemented.

----

**Original Solution Runtime:** `123ms` (Beats `5.12%`)
**Original Solution Memory:** `21.62mb` (Beats `12.73%`)



**Original Thoughts**

I'm not happy with this solution, and will probably revisit it in the future.
But I'm super limited on time today so this is what I got. 

The biggest annoyance in this problem was dealing with the list aliasing, mostly 
when memo-izing. I eventually gave in and just used deep copies. But I highly
doubt that's the best option here.

