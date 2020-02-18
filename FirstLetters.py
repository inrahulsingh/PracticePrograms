#Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
nst=st.split()
lst = [i[0] for i in nst]
print(lst)
