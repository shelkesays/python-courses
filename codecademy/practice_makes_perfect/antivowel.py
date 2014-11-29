def anti_vowel(text):
    vowels = "aeiouAEIOU"
    new_text = ""
    for char in text:
        if char not in vowels:
            new_text += char
    return new_text


print anti_vowel("Hey You! what are you doing?")
