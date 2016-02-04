file = open("sample.txt", "r")
text = file.read().lower().replace("\n", " ").replace(".", " ").replace("?", " ").replace("-", " ").replace(",", " ").replace(":", " ").replace("!", " ").replace("--", " ").replace(";", " ")
file.close()
word_list = text.lower().split(None)
word_freq = {}
for word in word_list:
    word_freq[word] = word_freq.get(word, 0) + 1
keys = sorted(word_freq.keys())
for word in keys:
    print("%-10s %d" % (word, word_freq[word]))
