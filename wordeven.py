#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
nst = st.split()
for i in nst:
    if len(i)%2==0:
        print(i,' -- length is even')
