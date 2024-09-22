"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
"""
class Solution:
    def findSubstring(self, S, L):
        if not L or not L[0]: return None
        a = len(L[0])
        totl = len(L) * a
        count_t = collections.defaultdict(int)
        for word in L: count_t[word] += 1
        r = []
        for i in range(a):
            count = copy.copy(count_t)
            j = i
            while j < len(S)-a+1:
                count[S[j:j+a]] -= 1
                while count[S[j:j+a]] < 0:
                    count[S[i:i+a]] += 1
                    i += a
                j += a
                if j-i == totl: r.append(i)
        return r

