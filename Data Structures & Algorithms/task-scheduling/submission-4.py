class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        max_count = sum([1 if f == max_freq else 0 for f in freq.values()])
        print(f'{max_count=} {max_freq=}')

        return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)

        # A   A   A   A   B   B   B   B   C   C       max_f = 4   max_c = 2   n = 3

        # A B C i     A B i i     A B i i     A B
        