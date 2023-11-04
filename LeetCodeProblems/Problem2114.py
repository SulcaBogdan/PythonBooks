from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        #Am dat split la fiecare propozitie din lista pentru a crea alte liste cu fiecare cuvant separat
        #Apoi am verificat fiecare lungime cu valoarea lui count si daca lungimea listei > count atunci count devine acea lungime
        #Time complexity O(n)
        for sentance in sentences:
            words = sentance.split(" ")
            if len(words) > count:
                count = len(words)
        return count