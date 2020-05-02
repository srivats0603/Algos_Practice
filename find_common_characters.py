class Solution_common_characters:
    def character_dict(self,elem):
        elem_dict = {}
        len_elem = len(elem)
        for i in range(0,len_elem):
            if elem[i] in elem_dict.keys():
                elem_dict[elem[i]] += 1
            else:
                elem_dict[elem[i]] = 1
        return elem_dict
    
    def commonChars(self, A: List[str]) -> List[str]:
        len_A = len(A)
        char_dict = self.character_dict(A[0])
        repeat_dict = {}
        for i in range(1,len_A):
            #print("\n comparing element {} with {}".format(i,i-1))
            len_elem = len(A[i])
            for j in range(0,len_elem):
                if (A[i][j] in char_dict) and (char_dict[A[i][j]]>0):
                    char_dict[A[i][j]] = char_dict[A[i][j]]-1
                    if A[i][j] in repeat_dict.keys():
                        repeat_dict[A[i][j]] += 1
                    else:
                        repeat_dict[A[i][j]] = 1
                    #print("new character_dict",char_dict)
                    #print("new repeat_dict",repeat_dict)
            char_dict = repeat_dict
            repeat_dict = {}   
        return_list = []
        for key in char_dict.keys():
            for j in range(0,char_dict[key]):
                return_list.append(key)
        
        return return_list
        
            