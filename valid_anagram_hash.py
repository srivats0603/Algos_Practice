class Solution_anagram_hashmap:
    def __init__(self):
      pass
    
    def build_character_map(self,s):
      character_dict = {}
      for i in range(0,len(s)):
        if s[i] not in character_dict.keys():
          character_dict[s[i]] = 1
        else:
          character_dict[s[i]] = character_dict[s[i]]+1
      return character_dict
      
    def isAnagram(self, s, t):
      #building a hashmap of the characters of s
      if len(s)!= len(t):
        return False
      character_dict = self.build_character_map(s)
      print("original character dict",character_dict)
      for j in range(0,len(t)):
        if t[j] not in character_dict.keys():
          return False
        elif character_dict[t[j]] < 1:
          return False
        elif character_dict[t[j]] >= 1:
          character_dict[t[j]] = character_dict[t[j]]-1
      
      print("final character dict", character_dict)
      if sum(character_dict.values()) == 0:
        return True
      else:
        return False