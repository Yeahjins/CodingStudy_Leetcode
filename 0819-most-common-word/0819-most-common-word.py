class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        x_list = [word for word in re.sub('[^A-Za-z0-9]', ' ', paragraph.lower()).split() if word not in banned]

        counts=collections.Counter(x_list)
        return counts.most_common()[0][0]