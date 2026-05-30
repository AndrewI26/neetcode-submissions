class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_to_group: dict[str, List[str]] = {}

        for word in strs:
            freq = [0 for _ in range(26)]
            for letter in word:
                freq[ord(letter) % 26] += 1
            freq_string = ""
            for count in freq:
                freq_string += str(count) + "-"

            freq_to_group[freq_string] = freq_to_group.get(freq_string, []) + [word]

        res = []
        for val in freq_to_group.values():
            res.append(val)
        return res

            
            
