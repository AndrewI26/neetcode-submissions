class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # [0, 0, 0 ... ] each pos shows letter freq
        acc = {} # freq arr -> [words]

        for string in strs:
            freq_arr = [0 for i in range(26)]
            for char in string:
                freq_arr[ord(char) % 26] += 1
            
            freq_hash_key = ""
            for num in freq_arr:
                freq_hash_key += str(num)

            if freq_hash_key in acc.keys():
                acc[freq_hash_key].append(string)
            else:
                acc[freq_hash_key] = [string]
        
        res = []
        for v in acc.values():
            res.append(v)
        return res