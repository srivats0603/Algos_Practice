class Solution_anagram:
    def __init__(self):
      pass
    
    def isAnagram(self, s, t):
      if len(s)!= len(t):
        return False
      else:
        while(len(s)>0):
          print("s =", s)
          print("t =", t)
          char_found = 0
          len_t = len(t)
          for i in range(0,len_t):
            print("s_0=",s[0])
            print("t_i=",t[i])
            if s[0] == t[i]:
              s = s[1:]
              if i<(len_t-1):
                t = t[0:i]+t[(i+1):len_t]
                len_t = len(t)
              elif i == (len_t-1):
                t = t[0:i]
                len_t = len(t)
              char_found = 1
              print("new s",s)
              print("new t",t,'\n')
              break
          if char_found == 0:
            return False
        return True