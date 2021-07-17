
# *There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

# You have to form a team of 3 soldiers amongst them under the following rules:

# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

# https://leetcode.com/problems/count-number-of-teams/

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n=len(rating)
        up =[0]*n
        down = [0]*n
        teams = 0
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if rating[i] < rating[j]:
                    up[i] +=1
                    teams += up[j]
                else:
                    down[i] +=1
                    teams += down[j]
        return teams
      
