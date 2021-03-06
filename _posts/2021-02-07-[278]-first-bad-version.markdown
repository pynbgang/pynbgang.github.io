---
layout: post
title: "[278] First Bad Version"
published: true
created:  2021 Feb 07 17:44:12
tags: [python, leetcode, easy]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [[278] First Bad Version](https://leetcode.com/problems/first-bad-version/description/)

    || * algorithms
    || * Easy (36.90%)
    || * Likes:    1946
    || * Dislikes: 796
    || * Total Accepted:    525.1K
    || * Total Submissions: 1.4M
    || * Testcase Example:  '5\n4'
    || * Source Code:       278.first-bad-version.py
    || 
    || You are a product manager and currently leading a team to develop a new
    product. Unfortunately, the latest version of your product fails the
    quality check. Since each version is developed based on the previous
    version, all the versions after a bad version are also bad.
    || 
    || Suppose you have n versions [1, 2, ..., n] and you want to find out the
    first bad one, which causes all the following ones to be bad.
    || 
    || You are given an API bool isBadVersion(version) which returns whether
    version is bad. Implement a function to find the first bad version. You
    should minimize the number of calls to the API.
    || 
    ||  
    || Example 1:
    || 
    || Input: n = 5, bad = 4
    || Output: 4
    || Explanation:
    || call isBadVersion(3) -> false
    || call isBadVersion(5) -> true
    || call isBadVersion(4) -> true
    || Then 4 is the first bad version.
    || 
    || Example 2:
    || 
    || Input: n = 1, bad = 1
    || Output: 1
    || 
    || Constraints:
    || 	1 <= bad <= n <= 2^31 - 1

# solution


```python
class Solution:     #lmv
    def firstBadVersion(self, n):
        l, r = 0, n-1
        while(l<=r):
            mid = l + (r-l)//2
            if isBadVersion(mid):
                r = mid-1
            else:
                l = mid+1
        return l
```
