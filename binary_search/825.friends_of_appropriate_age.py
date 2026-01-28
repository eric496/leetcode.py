"""_summary_
There are n persons on a social media website. You are given an integer array ages where ages[i] is the age of the ith person.
A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:
    age[y] <= 0.5 * age[x] + 7
    age[y] > age[x]
    age[y] > 100 && age[x] < 100
Otherwise, x will send a friend request to y.
Note that if x sends a request to y, y will not necessarily send a request to x. Also, a person will not send a friend request to themself.
Return the total number of friend requests made.

Example 1:
Input: ages = [16,16]
Output: 2
Explanation: 2 people friend request each other.

Example 2:
Input: ages = [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.

Example 3:
Input: ages = [20,30,100,110,120]
Output: 3
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.

Constraints:
    n == ages.length
    1 <= n <= 2 * 104
    1 <= ages[i] <= 120

"""


# Solution 1
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0] * 121
        for age in ages:
            count[age] += 1
        
        res = 0
        for age_x, count_x in enumerate(count):
            for age_y, count_y in enumerate(count):
                if age_y <= 0.5 * age_x + 7:
                    continue

                if age_y > age_x:
                    continue
                
                res += count_x * count_y

                if age_x == age_y:
                    res -= count_x
                
        return res
    
    
    # Solution 2: prefix sum 
    class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        count = [0] * 121
        for age in ages:
            count[age] += 1
        
        # Precompute prefix sums so we can calculate range sums in O(1)
        # prefix_sum[i] = total people with age <= i
        prefix_sum = [0] * 121
        cur = 0
        for i in range(121):
            cur += count[i]
            prefix_sum[i] = cur
            
        res = 0
        for age_x in range(15, 121): # Ages < 15 cannot make requests (formula < 15)
            if count[age_x] == 0: continue
            
            # Calculate the valid range for y
            min_age_y = int(0.5 * age_x + 7) # floor logic
            
            # We need sum of people in range (min_age_y, age_x]
            # Which is: prefix_sum[age_x] - prefix_sum[min_age_y]
            count_y_in_range = prefix_sum[age_x] - prefix_sum[min_age_y]
            
            # Add requests: (people of age_x) * (valid targets)
            # Subtract count[age_x] because people can't request themselves 
            # (they are included in the valid target range)
            res += count[age_x] * (count_y_in_range - 1)
            
        return res
    