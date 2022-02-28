class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        list_to_string = ''.join(map(str, digits)) #"123"
        string_to_int = int(list_to_string) + 1  #124

        int_to_string = str(string_to_int) # "124"
        int_to_list = list(map(int, int_to_string))

        return int_to_list