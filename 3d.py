text = input("Введите текст: ")
text = text.lower()
for p in "!\"#$%&()*+,-./:;<=>?@[\\]^_`{|}~":
    text = text.replace(p, "")
words = text.split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
most_common_word = max(word_counts, key=word_counts.get)
longest_word = max(words, key=len)
print("Наиболее часто встречающееся слово: ", most_common_word)
print("Самое длинное слово: ", longest_word)
