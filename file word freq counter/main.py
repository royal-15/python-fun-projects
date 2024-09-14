def words_counter(file_path):
    with open(file_path, "r") as file:
        data = file.read()
        words_in_data = data.split()
        # print(words_in_data)
        word_freq = {}
        for word in words_in_data:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    return word_freq

list = words_counter("check.txt")
for l,c in list.items():
    print(l,":",c)


