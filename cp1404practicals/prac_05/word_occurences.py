input_count = {}
input_text = input("Type something! \n> ")
words = input_text.split()

for word in words:
    count = input_count.get(word, 0)
    input_count[word] = count + 1

words = list(input_count.keys())
words.sort()
greatest_len = max((len(word) for word in words))

for word in words:
    print("{0:{1}} : {2}".format(word,greatest_len, input_count[word]))
