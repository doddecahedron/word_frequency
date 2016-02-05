file = open("sample.txt", "r")
text = file.read().lower().replace("\n", " ").replace(".", " ").replace("?", " ").replace("-", " ").replace(",", " ").replace(":", " ").replace("!", " ").replace("--", " ").replace('"', " ").replace(";", " ").split(' ')
file.close()
word_list = text
word_freq = {}

for line in text:
    words = line.split()
    for word in words:
        k = word.lower()
        if "'" in k:
            ks = k.split("'")
        else:
            ks = [k, ]
        for k in ks:
            word_freq[k] = word_freq.get(k, 0) + 1
for word in sorted(word_freq, key=lambda k: word_freq[k], reverse=True)[:20]:
    print(word, "\t", word_freq[word])