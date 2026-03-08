**Solution Runtime:** `148ms` (Beats `45.73%`)
**Solution Memory:** `43.18mb` (Beats `22.59%`)

**Thoughts**

My initial thought was just to sort and check adjacent elements. But then 
realized we only need some sets. Which uses more memory but makes it more 
time-efficient (at least in theory).

There's definitely optimizations here. Some memory efficiency between the `seen` and
`lonelyNumbers` sets, *mayybe* getting rid of one of them and instead keeping a
store of indices to remove (not convinced by that). 

Time performance-wise, because the constraints restrict the size of numbers to 
the same range as the list size, I could see sorting actually being more efficient
if we do some smart skipping.
