class Solution {
    func isPowerOfTwo(_ n: Int) -> Bool {
        if n == 0{
            return false
        }else{
            return (n & (n - 1)) == 0        
        }
    }
}
