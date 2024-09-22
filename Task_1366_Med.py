"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/rank-teams-by-votes/description/
"""
class Solution(object):
    def rankTeams(self, votes):
        counts = collections.defaultdict(list)
        for vote in zip(*votes):
            c = collections.Counter(vote)
            for b in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                counts[b] += [-1*c[b]]
        return "".join(sorted(votes[0],key=lambda x :counts[x]+[x]))



