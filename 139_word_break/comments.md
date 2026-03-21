**Solution Runtime:** `0ms` (Beats `100%`)
**Solution Memory:** `19.51mb` (Beats `24.43%`)



**Thoughts**

Again, it seems like an easy medium problem. The only notable decisions are to
keep track of which end segments cannot be finished, and then try to depth first
as quick as possible to find those unfinishable segments. But after the first
observation, the second one was pretty immediate. 