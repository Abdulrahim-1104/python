# print(len("------------------j------------------"))
# s="cabac"
# print(reversed(s))
# print(s[len(s):len(s)//2:-1])
# original_string = "c"
# separator = "d"
# joined_string = separator.join(original_string)
# print(joined_string)
# print("a-b-b".center(9,'-'))
# s='cbc'
# print(s[:len(s)//2+1]+'d'+s[(len(s)//2)::-1])
# print(chr(99))
# print(len('------------------j------------------'))
# print('-'.join('c'))
n=5
def print_rangoli(n):
    # your code goes here
    str = ''
    for i in range(n * 2 -1):
        if i <= n - 1:
            char = chr(96 + n - i)
            str = str[:len(str)//2+1] + char + str[(len(str)//2)::-1]
            s = '-'.join(str)
        else:
            s = s[:len(s)//2] + s[len(s)//2+4:]
        print(s.center(n*4-3,'-'))
print_rangoli(3)

