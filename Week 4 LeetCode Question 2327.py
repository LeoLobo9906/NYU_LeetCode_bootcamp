#2327 Number of people aware of a secret
"""
On day 1, one person discovers a secret.
You are given an integer delay, which means that each person will share the secret with a new person every day, starting from delay days after discovering the secret. You are also given an integer forget, which means that each person will forget the secret forget days after discovering it. A person cannot share the secret on the same day they forgot it, or on any day afterwards.
Given an integer n, return the number of people who know the secret at the end of day n. Since the answer may be very large, return it modulo 109 + 7.

Example 2:

Input: n = 4, delay = 1, forget = 3
Output: 6
Explanation:
Day 1: The first person is named A. (1 person)
Day 2: A shares the secret with B. (2 people)
Day 3: A and B share the secret with 2 new people, C and D. (4 people)
Day 4: A forgets the secret. B, C, and D share the secret with 3 new people. (6 people)

Constraints:

2 <= n <= 1000
1 <= delay < forget <= n
"""

def peopleAwareOfSecret(self, n, delay, forget):
    dp = [1] + [0] * (n - 1)
    mod = 10 ** 9 + 7
    share = 0
    for i in range(1, n):
        dp[i] = share = (share + dp[i - delay] - dp[i - forget]) % mod
    return sum(dp[-forget:]) % mod


