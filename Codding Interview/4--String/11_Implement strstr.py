'''
	Your task is to return the index of the pattern
	present in the given string.

	Function Arguments: s (given text), p(given pattern)
	Return Type: Integer.

'''


def strstr(s, p):
    # code here
    try:
        return s.index(p)
    except:
        return -1


# {
#  Driver Code Starts
# Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        s, p = input().strip().split()
        print(strstr(s, p))

# } Driver Code Ends