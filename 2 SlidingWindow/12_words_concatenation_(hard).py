from typing import List


class words_concatenation:
    def find_word_concatenation(s: str, words) -> List[int]:
        if len(s) < (len(words) * len(words[0])):
            return []
        words_frequency = {}
        result = []

        for word in words:
            words_frequency[word] = 1 + words_frequency.get(word, 0)
        words_count = len(words)
        word_len = len(words[0])
        for i in range((len(s) - word_len * words_count) + 1):
            words_seen = {}
            for j in range(0, words_count):
                next_word_index = i + j * word_len
                word = s[next_word_index:next_word_index + word_len]
                if word not in words_frequency:
                    break
                words_seen[word] = 1 + words_seen.get(word, 0)
                if words_seen[word] > words_frequency.get(word, 0):
                    break
                if j + 1 == words_count:
                    result.append(i)

        return result




if __name__ == '__main__':
    sol = words_concatenation
    print("Expected [0,3] Actuat: " + str(sol.find_word_concatenation("catfoxcat", ["cat", "fox"])))
    print("Expected [0,9] Actuat: " + str(sol.find_word_concatenation("barfoothefoobarman", ["foo", "bar"])))
    print("Expected [] Actuat: " + str(sol.find_word_concatenation("wordgoodgoodgoodbestword", ["word", "good", "best", "word"])))
    print("Expected [6,9,12] Actuat: " + str(sol.find_word_concatenation("barfoofoobarthefoobarman", ["bar", "foo", "the"])))

