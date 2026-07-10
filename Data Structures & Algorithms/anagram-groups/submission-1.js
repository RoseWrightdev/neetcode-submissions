class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let hm = {}
        for (const str of strs) {
            let counts = new Array(26).fill(0)
            for (const ch of str) {
                let index = ch.charCodeAt(0) - 'a'.charCodeAt(0)
                counts[index]++
            }
            const key = counts.join(',');
            if (!hm[key]) {
                hm[key] = [];
            }
            hm[key].push(str);
        }
        return Object.values(hm);

    }
}
