class Solution {
    func countSegments(_ s: String) -> Int {
        var res = s.split(separator: " ")
        return res.count
    }
}
