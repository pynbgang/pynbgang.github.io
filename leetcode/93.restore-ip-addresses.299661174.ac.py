#
# @lc app=leetcode id=93 lang=python
#
# [93] Restore IP Addresses
#


class Solution(object):
  def restoreIpAddresses(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    res = []
    for i in [1, 2, 3]:
      for j in [i+1, i+2, i+3]:
        for k in [j+1, j+2, j+3]:
          if k >= len(s):
            break
          s1, s2, s3, s4 = s[:i], s[i:j], s[j:k], s[k:]
          add_ip = True
          for st in [s1, s2, s3, s4]:
            if (st != "0" and st[0] == "0") or int(st) > 255:
              add_ip = False
              break
          if add_ip:
            res.append(s1+"."+s2+"."+s3+"."+s4)
    return res

#(Sat 29 Aug 2020 04:45:32 PM DST)
class Solution(object):
  def restoreIpAddresses(self, s):
    res = []
    for i in [1,2,3]:
      for j in [i+1, i+2, i+3]:
         for k in [j+1, j+2, j+3]:
           ip1, ip2, ip3, ip4 = s[:i], s[i:j], s[j:k], s[k:]
           if all(len(ip)>0 and int(ip) <= 255 and (ip[0] != '0' if len(ip) > 1 else True) for ip in [ip1, ip2, ip3, ip4]):
             res.append(ip1 + "." + ip2 + "." + ip3 + "." + ip4)
    return res


class Solution(object):
  def restoreIpAddresses(self, s):
    return [
      s[:i] + "." + s[i:j] + "." + s[j:k] + "." + s[k:]
      for i in [1,2,3] for j in [i+1, i+2, i+3] for k in [j+1, j+2, j+3]
      if all(
        len(ip)>0 and
        int(ip) <= 255 and
        (ip[0] != '0' if len(ip) > 1 else True)
        for ip in [s[:i], s[i:j], s[j:k], s[k:]]
      )
    ]
#(Sat 29 Aug 2020 05:32:07 PM DST)
