#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    name1=name[0:3].capitalize()
    name2=name[3:].capitalize()
    return name1+name2

result=old_macdonald('macdonald')
print(result)
