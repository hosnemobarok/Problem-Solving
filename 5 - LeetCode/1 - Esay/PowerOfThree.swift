class Solution {
    func isPowerOfThree(_ n: Int) -> Bool {
        var res = n
        if res < 1{
            return false
        }
        else{
            while (res % 3 == 0) {
                res /= 3
            }
            return res == 1
        }
    }
}
