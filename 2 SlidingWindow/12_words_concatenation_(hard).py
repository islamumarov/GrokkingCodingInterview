def find_word_concatenation(str, words):
    result_indices = []
    word_frequency = {}
    for word in words:
        word_frequency[word] = 1 + word_frequency.get(word, 0)
    words_count = len(words)
    word_len = len(words[0])
    for i in range((len(str) - word_len * words_count) + 1):
        words_seen = {}
        for j in range(0, words_count):
            next_word_index = i + j * word_len
            word = str[next_word_index: next_word_index + word_len]
            if word not in word_frequency:
                break
            words_seen[word] = 1 + words_seen.get(word, 0)
            if words_seen[word] > word_frequency.get(word, 0):
                break
            if j + 1 == words_count:
                result_indices.append(i)

    return result_indices


if __name__ == '__main__':
    print("Expected [0,3] Actuat: " + str(find_word_concatenation("catfoxcat", ["cat", "fox"])))
    print("Expected [0,9] Actuat: " + str(find_word_concatenation("barfoothefoobarman", ["foo", "bar"])))
    print("Expected [] Actuat: " + str(find_word_concatenation("wordgoodgoodgoodbestword", ["word", "good", "best", "word"])))
    print("Expected [6,9,12] Actuat: " + str(find_word_concatenation("barfoofoobarthefoobarman", ["bar", "foo", "the"])))

