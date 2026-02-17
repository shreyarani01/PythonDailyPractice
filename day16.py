def pallindrome(text):
    if len(text) <= 1:
        print("pallindrome")
    else:
        if text[0] == text[-1]:
            pallindrome(text[1:-1]) 
        else:
            print("not a pallindrome")
pallindrome("madam")
pallindrome("abba")
pallindrome("python")