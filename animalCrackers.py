#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    textl=text.split()
    if textl[0][0]==textl[1][0]:
        return True
    else:
        return False


result=animal_crackers('Doing Not')
print(result)
