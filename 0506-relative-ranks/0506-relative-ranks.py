class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        a = score.copy()
        a.sort(reverse=True)
        for i in range(len(a)):
            if i == 0:
                score[score.index(a[i])] = "Gold Medal"
            elif i == 1:
                score[score.index(a[i])] = "Silver Medal"
            elif i == 2:
                score[score.index(a[i])] = "Bronze Medal"
            else:
                score[score.index(a[i])] = str(i+1)
        return score