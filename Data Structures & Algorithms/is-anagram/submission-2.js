class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let counts = new Array(26).fill(0)
        for (const ch of s) {
            let index = ch.charCodeAt(0) - "a".charCodeAt(0)
            counts[index]++
        }

        for (const ch of t) {
            let index = ch.charCodeAt(0) - "a".charCodeAt(0)
            counts[index]--
            if (counts[index] < 0) {
                return false
            }
        }

        for (const num of counts) {
            if (num != 0) {
                return false
            }
        }
        return true
    }
}
