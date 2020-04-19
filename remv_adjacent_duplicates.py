class Solution_rmv_adj_dup:
    def method_stack(self,S,len_S):
        string_stack = deque([])
        for i in range(0,len_S):
            if (len(string_stack) == 0) or (string_stack[-1] != S[i]):
                string_stack.append(S[i])
            elif (string_stack[-1] == S[i]):
                string_stack.pop()
        return("".join(string_stack))
    
    def method_modify_string(self,S,len_S):
        new_string = ""
        len_new_string = 0
        for i in range(0,len_S):
            if len_new_string == 0:
                new_string += S[i]
                len_new_string +=1
            elif (new_string[len_new_string-1] != S[i]):
                new_string += S[i]
                len_new_string +=1
            elif (new_string[len_new_string-1] == S[i]):
                len_new_string = len_new_string-1
                new_string = new_string[0:len_new_string]
        return new_string
    
    def removeDuplicates(self, S: str) -> str:
        len_S = len(S)
        if len_S == 1:
            return S
        #return self.method_stack(S,len_S)
        return self.method_modify_string(S,len_S)