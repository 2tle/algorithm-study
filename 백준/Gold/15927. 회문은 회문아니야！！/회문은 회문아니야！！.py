import sys

input = sys.stdin.readline

def isPalindrome(string):
    length = len(string) // 2
    rlen = len(string) -1
    for x in range(0, length):
        if string[x] != string[rlen-x]:
            return False
    return True

inp = input().rstrip()
#if len(inp) == 1:
#    print(-1)
#elif isPalindrome(inp) == False:
#    print(len(inp))
#elif isPalindrome(inp[0:-2]) == False:
#    print(len(inp)-1)
#else:
#    print(-1)


if len(inp) == 1 or len(set(inp)) == 1:
    print(-1)
elif isPalindrome(inp):
    print(len(inp) - 1)
else:
    print(len(inp))


# ABCBA -> 4
# ABCDEDCBA -> 8
# AABBCBBAA -> 8
# AAAAAA -> -1
# 