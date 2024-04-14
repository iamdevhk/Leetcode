class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringsResult=dict()
        for string in strs:
            sorted_String=''.join(sorted(string)) #sort the string
            if sorted_String not in stringsResult: # if sorted string not in dict create that empty list
                stringsResult[sorted_String]=[]
            stringsResult[sorted_String].append(string) #append the string to that if its already in it
        return list(stringsResult.values()) #return only the values and not teh keys
        