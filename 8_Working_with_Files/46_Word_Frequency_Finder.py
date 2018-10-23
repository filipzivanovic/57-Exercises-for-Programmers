with open("46_words", "r") as f:
    lines = f.readlines()

for line in lines:
    print(line.strip())

word_list = []
for line in lines:
    for char in '-.,\n':
        line = line.replace(char, ' ')
    line = line.lower()
    word_list.extend(line.split())

print(word_list)

d = {}
for word in word_list:
    if word not in d:
        d[word] = 0
    d[word] += 1

word_freq = []
for key, value in d.items():
    word_freq.append((value, key))
word_freq.sort(reverse=True)

print(word_freq)

print('Word            | Frequency          ')
print('----------------|--------------------')
for k, v in word_freq:
    print('{word:15} | {frequency:25}'.format(word=v, frequency=k * '*'))
