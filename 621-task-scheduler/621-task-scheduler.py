class Solution:
	def leastInterval(self, tasks: List[str], n: int) -> int:
		if n == 0: 
			return len(tasks)
		frequency = Counter(tasks)

		hf = max(frequency.values())

		count = 0
		for task, occ in frequency.items():
			if occ == hf:
				count += 1


		gap = (hf-1)*(n+1) + count

		return max(gap, len(tasks))