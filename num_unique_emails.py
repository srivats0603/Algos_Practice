class Solution_numUniqueEmails:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_email_dict = {}
        num_Unique_Emails = 0
        for elem in emails:
            [first_name,domain_name] = elem.split('@')
            if '+' in first_name:
                first_name = first_name.split('+')[0]
            if '.' in first_name:
                first_name =''.join(first_name.split('.'))
            this_final_name = first_name+'@'+domain_name
            if this_final_name not in unique_email_dict.keys():
                num_Unique_Emails += 1
                unique_email_dict[this_final_name]= num_Unique_Emails
        print(unique_email_dict)
        return num_Unique_Emails