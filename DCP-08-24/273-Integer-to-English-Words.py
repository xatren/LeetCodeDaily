class Solution(object):
    def numberToWords(self, num):
        \\\
        :type num: int
        :rtype: str
        \\\
        if num == 0:
            return \Zero\
        
        def one(num):
            switch = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            return switch.get(num)
        
        def two_less_20(num):
            switch = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return switch.get(num)
        
        def ten(num):
            switch = {
                20: 'Twenty',
                30: 'Thirty',
                40: 'Forty',
                50: 'Fifty',
                60: 'Sixty',
                70: 'Seventy',
                80: 'Eighty',
                90: 'Ninety'
            }
            return switch.get(num)
        
        def two(num):
            if not num:
                return ''
            elif num < 10:
                return one(num)
            elif num < 20:
                return two_less_20(num)
            else:
                tenner = num // 10 * 10
                rest = num % 10
                return ten(tenner) + (' ' + one(rest) if rest else '')
        
        def three(num):
            hundred = num // 100
            rest = num % 100
            if hundred and rest:
                return one(hundred) + ' Hundred ' + two(rest)
            elif not hundred and rest:
                return two(rest)
            elif hundred and not rest:
                return one(hundred) + ' Hundred'
        
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        remainder = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        
        result = ''
        if billion:
            result += three(billion) + ' Billion'
        if million:
            if result:
                result += ' '
            result += three(million) + ' Million'
        if thousand:
            if result:
                result += ' '
            result += three(thousand) + ' Thousand'
        if remainder:
            if result:
                result += ' '
            result += three(remainder)
        
        return result
