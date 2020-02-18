def myfunc(mystring):
    result=''
    for i in range(len(mystring)):
        if i % 2 == 0:
            result += mystring[i].upper()
        else:
            result += mystring[i].lower()
    return result
