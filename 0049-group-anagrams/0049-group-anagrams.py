class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        q_dict={}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in q_dict:
                q_dict[sorted_word] = []
            q_dict[sorted_word].append(word)

        result = list(q_dict.values())
        return result