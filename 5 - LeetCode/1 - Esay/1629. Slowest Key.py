class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_cnt = prev = 0
        cnt = [0] * 26
        ans = 'z'
        for t, k in zip(releaseTimes, keysPressed):
            cur_cnt = cnt[ord(k)-ord('a')] = max(cnt[ord(k)-ord('a')], t-prev)
            prev = t
            if max_cnt<cur_cnt or max_cnt==cur_cnt and ans<k:
                ans = k
                max_cnt = cur_cnt
        return ans