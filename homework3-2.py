f = open('big text file.txt','r')
a = f.read()
f.close()

a = a.replace(',','')
a = a.replace('.','')
a = a.replace('!','')
a = a.replace('?','')
a = a.lower()
vocabulary = a.split(' ')
vocabulary_set = set()
for i in range(len(vocabulary)):
    vocabulary_set.add(vocabulary[i])
word_freq = []
for i in vocabulary_set:
    word_freq.append([vocabulary.count(i),i])

sorted_word_freq = []
max = 0
max_index = 0
while len(word_freq) > 0:
    for i in range(len(word_freq)):
        if word_freq[i][0] > max:
            max = word_freq[i][0]
            max_index = i
    sorted_word_freq.append(word_freq.pop(max_index))
    max_index = 0
    max = 0
top = 10
if len(sorted_word_freq) < top:
    top = len(sorted_word_freq)
for i in range(top):
    print(i + 1, sorted_word_freq[i])
