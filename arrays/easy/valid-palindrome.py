# https://leetcode.com/problems/valid-palindrome/description/

def isPalindrome(s):
    out = ""
    for i in range(0, len(s)):
        if 64 < ord(s[i]) < 91:
            out += chr(ord(s[i]) + 32)
        elif 47 < ord(s[i]) < 58 or 96 < ord(s[i]) < 123:
            out += s[i]
    i = 0
    j = len(out) - 1
    while i < j:
        if out[i] != out[j]:
            return False
    else:
        return True


def isPalindrome_1(s):
    out = s
    formatted_string = ''.join(filter(str.isalnum, out.lower()))
    reverse_string = formatted_string[::-1]
    if reverse_string == formatted_string:
        return True
    return False


print(isPalindrome_1("Hey, 3how are you3!"))
print(isPalindrome_1("A man, a plan, a canal: Panama"))
