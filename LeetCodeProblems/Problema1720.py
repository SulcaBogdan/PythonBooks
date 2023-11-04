from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        new_array = [first]
        for num in encoded:
            new_array.append(new_array[-1] ^ num)
        return new_array