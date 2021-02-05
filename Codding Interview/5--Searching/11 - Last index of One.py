
def Last_index_of_One(string):

    if '1' not in string:
        return -1

    index = -1
    for i in range(len(string)):
        if string[i] == '1':
            index = i

    return index


if __name__ == '__main__':
    string = input()
    print(Last_index_of_One(string))







"""# User function Template for python3

class Solution:
    def lastIndex(self, s):
        # code here
        if '1' not in s:
            return -1
        else:
            index = -1
            for i in range(len(s)):
                if s[i] == '1':
                    index = i

            return index


# { 
#  Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())

    while (T > 0):
        s = input()
        ob = Solution()
        print(ob.lastIndex(s))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends"""