class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        bank = set(bank)
        queue = deque([(start, 0)])

        while queue:
            cur, level = queue.popleft()
            if cur == end:
                return level
            for i, c in product(range(8), "AGCT"):
                mutation = cur[:i] + c + cur[i+1:]
                if mutation in bank:
                    bank.remove(mutation)
                    queue.append((mutation, level+1))
        return -1