class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let s = new Set()
        for (const num of nums) {
            if (s.has(num)) {
                return true
            }
            s.add(num)
        }
        return false
    }
}
