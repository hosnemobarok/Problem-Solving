"""
    https://leetcode.com/submissions/detail/769870326/
    
    Time complexity     : O(n)
    Space complexity    : O(1)
"""

class Solution {
    func isUgly(_ n: Int) -> Bool {

        if n == 1 { return true}
        if n == 0 { return false}
        var num = n

        while num >= 1{
            if num % 2 == 0{
                num /= 2

            }else if num % 3 == 0{
                num /= 3

            } else if num % 5 == 0 {
                num /= 5

            }else{ break }
        }

        return num == 1 ? true : false
    }
}
