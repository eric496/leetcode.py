"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:
Input: 123
Output: "One Hundred Twenty Three"

Example 2:
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""

class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"
        
        places = ['', 'Thousand', 'Million', 'Billion', 'Trillion']
        d = {
            0: '',
            1: 'One', 
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
            100: 'Hundred',
        }
        
        ls_res = []
        place_cnt = 0
        
        while num:
            cur_num = num % 1000
            cur_res = []
            hs = cur_num // 100
            ts = int(str(cur_num//10)[-1]) * 10
            os = cur_num % 10
            
            # Tenth place less than twenty
            if ts == 10:
                ts = ts + os
                os = 0
                    
            if hs:
                cur_res.append(d[hs])
                cur_res.append(d[100])
            if ts:
                cur_res.append(d[ts])
            if os:
                cur_res.append(d[os])
            
            ls_res.append(cur_res)
            
            # Less than one thousand or all places are zeros
            if place_cnt and cur_res:
                cur_res.append(places[place_cnt])
            
            num //= 1000
            place_cnt += 1
            
        res = []
        
        for ls in ls_res[::-1]:
            res.extend(ls)
            
        return ' '.join(res)
