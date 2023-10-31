def is_palindrome(s):
    s_l = len(s)
    for i in range(s):
        if s[i] != s[s_l -i -1]:
            return false
    return true
