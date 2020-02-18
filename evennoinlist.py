def myfunc(*args):
    mylist=[]
    for i in args:
        if i%2==0:
            mylist.append(i)
    return mylist
