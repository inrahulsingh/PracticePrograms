#MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    rtextlst=[]
    textlst=text.split()
    for i in reversed(textlst):
        rtextlst.append(i)
    return " ".join(rtextlst)

result=master_yoda('We are ready')
print(result)
        
