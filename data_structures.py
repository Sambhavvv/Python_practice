sentence = "this is nice"
list_of_words = []

word = ''

for i in sentence:
    if i != ' ':  
        word = word + i
    else:
        list_of_words.append(word)  
        word = ''  

if word:
    list_of_words.append(word)

print(list_of_words)

final = ''.join(list_of_words)
print(final)