def word_stats(sentence):
    words = sentence.split()
    print(f"Word count: {len(words)}")

    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word 
    print(f"Longest word: {longest}")


full_sentence = input("Sentence: ")
word_stats(full_sentence)
