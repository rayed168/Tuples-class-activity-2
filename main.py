def palindrome(tup):
    e=len(tup)-1
    s=0
    while s<e:
        if tup[s]!=tup[e]:
            return False
        s=s+1
        e=e-1
    return True
tup=(1,2,3,3,2,1)
if palindrome(tup):
    print("It is a palindrome")
else:
    print("It is not a palindrome")