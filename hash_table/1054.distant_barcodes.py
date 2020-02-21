"""
In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].
Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed an answer exists.

Example 1:
Input: [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]

Example 2:
Input: [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,2,1,2,1]

Note:
1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
"""


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = {}
        max_b = max_cnt = 0
        
        for b in barcodes:
            freq[b] = freq.get(b, 0) + 1
            if freq[b] > max_cnt:
                max_b, max_cnt = b, freq[b]
            
        pos = 0
        res = [0] * len(barcodes)
        
        # Fill in the barcode with top frequency
        while freq[max_b]:
            res[pos] = max_b
            freq[max_b] -= 1
            pos += 2
        
        # Remove the barcode with top frequency 
        # Fill in other barcodes
        freq.pop(max_b)
                
        for b in freq:
            while freq[b]:
                # Even index positions are all filled
                # Begin to fill in odd index positions
                pos = pos if pos < len(res) else 1
                res[pos] = b
                freq[b] -= 1
                pos += 2
        
        return res
