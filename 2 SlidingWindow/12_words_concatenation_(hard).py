

if __name__ == '__main__':
    print("Expected [0,3] Actuat: " + str(find_word_concatenation("catfoxcat", ["cat", "fox"])))
    print("Expected [0,9] Actuat: " + str(find_word_concatenation("barfoothefoobarman", ["foo", "bar"])))
    print("Expected [] Actuat: " + str(find_word_concatenation("wordgoodgoodgoodbestword", ["word", "good", "best", "word"])))
    print("Expected [6,9,12] Actuat: " + str(find_word_concatenation("barfoofoobarthefoobarman", ["bar", "foo", "the"])))

