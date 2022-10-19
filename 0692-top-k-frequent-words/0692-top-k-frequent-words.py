class Solution:
	def topKFrequent(self, words: List[str], k: int) -> List[str]:
		d = {}
		for word in words:
			if word not in d:
				d[word] = 1
			else:
				d[word] = d[word] + 1

		d = dict(sorted(d.items(), key = lambda item : item[0]))
		d = dict(sorted(d.items(), key = lambda item : item[1], reverse = True))
		result = []
        
		for key in d:
			if len(result) >= k:
				break
			result.append(key)
		return result