#Use for, .split(), and if to create a Statement that will print out words that start with 's':
st='Print only the words that start with s in this Sentence'
nst=st.split()
for nstw in nst:
    snstw=nstw.split()
    if snstw[0][0]=='s':
        print(snstw)
    elif snstw[0][0]=='S':
        print(snstw)
        
