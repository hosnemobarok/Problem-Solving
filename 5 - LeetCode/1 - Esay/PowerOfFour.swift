class Solution {
    func isPowerOfFour(_ n: Int) -> Bool {
        var res = n
        
        if res == 0{ 
            return false 
        }
        while (res % 4 == 0) {
            res /= 4
        }
        if res == 1{
            return true 
        }else{
            return false
        }
    }
}
