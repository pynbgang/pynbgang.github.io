---
layout: post
title: "lowercase-to-uppercase-ii"
published: true
date: 2020-02-10 
created:  2020 Feb 13 02:34:29 PM
tags: [python, easy, string, lintcode, leetcode, chr, ord, map, wangmazi, oneliner]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [lowercase-to-uppercase-ii](https://www.lintcode.com/problem/lowercase-to-uppercase-ii/description?_from=ladder&&fromId=99)

Description
Implement an upper method to convert all characters in a string to uppercase.

The characters not in alphabet don't need to convert

Example
Example 1:

Input: str = "abc"
Output: "ABC"
Example 2:

Input: str = "aBc"
Output: "ABC"
Example 3:

Input: str = "abC12"
Output: "ABC12"


similar to [leetcode](https://leetcode.com/problems/to-lower-case/description/)

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"

## ping

```python
class Solution:
    """
    @param str: A string
    @return: A string
    """
    def lowercaseToUppercase2(self, str):
        # write your code here
        str_new=""
        for c in str:
            str_new += chr(ord(c) - ord('a') + ord('A')) if c >= 'a' and c <= 'z' else c
            #if c >= 'a' and c <= 'z':
            #    str_new += chr(ord(c) - ord('a') + ord('A'))
            #    #str_new += chr(ord(c) - 32)
            #else:
            #    str_new += c
        return str_new

```

oneliner with `map`

```python
class Solution:
    def lowercaseToUppercase2(self, str):
	return join('', map(lambda c: chr(ord(c) - ord('a') + ord('A')) if c>='a' and c<='z' else c, str))
```

### tips

- use `chr` and `ord`
- '32' method: `ord('a')-ord('A')==32`
- offset method: `chr(ord(c) - ord('a') + ord('A'))`
- letter and strings compare

	[ins] In [11]: 'zbc' < 'zac'                      
	Out[11]: False

## wangmazi

```python
lass Solution:
    # @param {string} str a string
    # @return {string} a string
    def lowercaseToUppercase2(self, str):
        # Write your code here
        p = list(str)
        #遍历整个字符串，将所有的小写字母转成大写字母
        for i in range(len(p)):
            if p[i] >= 'a' and p[i] <= 'z':     #<---
                p[i] = chr(ord(p[i]) - 32)      #<---
        return ''.join(p)
```

