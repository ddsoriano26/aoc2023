## Part 1
- Can use `permutations` with restraint
	- For each permutation, check if replacing the non-dots are equal with the original
- Count remaining number of `#` needed
	- Replace `?` with `#` depending on the number, and then get the permutation
	- Check if permutation is possible
- `permutations` taking too long
	- How to do permutations or replacement in a loop with all restraints/considerations?
	- Permutate only `?`? And then put it back into the string