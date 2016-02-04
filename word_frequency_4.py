def most_common(h):
    t = []
    for key, value in h.items():
        t.append((value, key))

    t.sort(reverse=True)
    return t

t = most_common()
print('The most common words are:')
for freq, word in t[0:20]:
    print(word, '\t', freq)