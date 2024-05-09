class Solution:
    def maximumHappinessSum(self, happiness, k):
        ans = 0

        happiness.sort(reverse=True)

        decremented = [min(happiness[i], i) for i in range(len(happiness))]

        for i in range(k):
            ans += max(0, happiness[i] - decremented[i])

        return ans

