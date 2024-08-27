sen= "Bye Bye Bye Deadpool "
word=''
words=[]
for i in sen:
    if i!=' ':
        word=i+word
    else:
        words.append(word)
        word=''
print(words)
