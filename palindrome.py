def chkpal(s):
    s=s.replace(" ","")
    if s==s[::-1]:
        print(s,"is palindrome")
    else:
        print(s,"is not palindrome")

chkpal("abcba")
