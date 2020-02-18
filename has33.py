def has33(num):
    for i in range(0,len(num)-1):
        if num[i:i+2]==[3,3]:
            return True
    return False

result=has33([1,3,2,3])
print(result)
