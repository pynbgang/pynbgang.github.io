---
layout: post
title: "[13] Roman to Integer"
published: true
created:  2020 Mar 08 03:03:26 PM
tags: [python, leetcode, string, number, easy, replace]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[13] Roman to Integer](https://leetcode.com/problems/roman-to-integer/description/)

    || * algorithms
    || * Easy (54.32%)
    || * Likes:    1839
    || * Dislikes: 3248
    || * Total Accepted:    602.4K
    || * Total Submissions: 1.1M
    || * Testcase Example:  '"III"'
    || * Source Code:       13.roman-to-integer.py
    || 
    || Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    || 
    || Symbol       Value
    || I             1
    || V             5
    || X             10
    || L             50
    || C             100
    || D             500
    || M             1000
    || 
    || For example, two is written as II in Roman numeral, just two one's added
    together. Twelve is written as, XII, which is simply X + II. The number
    twenty seven is written as XXVII, which is XX + V + II.
    || 
    || Roman numerals are usually written largest to smallest from left to
    right. However, the numeral for four is not IIII. Instead, the number four
    is written as IV. Because the one is before the five we subtract it making
    four. The same principle applies to the number nine, which is written as
    IX. There are six instances where subtraction is used:
    || 
    || 
    || 	I can be placed before V (5) and X (10) to make 4 and 9. 
    || 	X can be placed before L (50) and C (100) to make 40 and 90. 
    || 	C can be placed before D (500) and M (1000) to make 400 and 900.
    || 
    || Given a roman numeral, convert it to an integer. Input is guaranteed to
    be within the range from 1 to 3999.
    || 
    || Example 1:
    || Input: "III"
    || Output: 3
    || 
    || Example 2:
    || Input: "IV"
    || Output: 4
    || 
    || Example 3:
    || Input: "IX"
    || Output: 9
    || 
    || Example 4:
    || Input: "LVIII"
    || Output: 58
    || Explanation: L = 50, V= 5, III = 3.
    || 
    || Example 5:
    || Input: "MCMXCIV"
    || Output: 1994
    || Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

## lmv: convert all substraction to addition

```python
class Solution:     #lmv: convert all substraction to addition
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
```

## wangmazi: compare adjacent nums to decide - or +
```python
class Solution:     #wangmazi, compare adjacent nums to decide - or +
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        if s == "":
            return 0
        index = len(s) - 2
        sum = ROMAN[s[-1]]
        while index >= 0:
            if ROMAN[s[index]] < ROMAN[s[index + 1]]:
                sum -= ROMAN[s[index]]
            else:
                sum += ROMAN[s[index]]
            index -= 1
        return sum

```

## tips

* replace.replace.replace
