"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Given an integer, convert it to a roman numeral.
"""


class Solution:
    def into_roman(self, num: int) -> str:
        hashmap = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                   5: 'V', 4: 'IV', 1: 'I', }
        num_in_roman = []
        number = num
        for x in hashmap:
            while number >= x:
                num_in_roman.append(hashmap[x])
                number -= x

        final = ''.join(num_in_roman)

        return final


class SolutionUpgraded:

    @staticmethod
    def into_roman(num: int) -> str:

        hashmap = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                   5: 'V', 4: 'IV', 1: 'I', }
        num_in_roman = ''
        number = num
        for x in hashmap:
            while number >= x:
                num_in_roman += hashmap[x]
                number -= x

        return num_in_roman


trythisshit = SolutionUpgraded
trythisshit.into_roman(3)

