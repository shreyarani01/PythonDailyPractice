# fibonacci using memorization 

def memo(m,d):
     # d = dictionary
    if m in d:
        return d[m]
    else:
        d[m] = memo(m-1,d) + memo(m-2,d)
    return d[m]

d = {0:1,1:1} # base case when m =0 return 1 and m=1 return 1
print(memo(500,d))