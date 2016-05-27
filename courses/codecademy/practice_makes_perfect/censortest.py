def censor(text, word):
    words = text.split()
    for index, w in enumerate(words):
        if word.lower() == w.lower():
            words[index] = "*" * len(word)
    return ' '.join(words)


print censor("Hey this is Hey wired hey hey he", "hey")
