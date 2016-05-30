def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

def remove_special_chars(text):
    stop_words = [' ', ',', '.', '!', '?']
    for stop in stop_words:
        text = text.replace(stop, '')
    return text  # .translate(''.join(stop_words))

something = input("Enter text: ")
something = remove_special_chars(something)
print(something)
if is_palindrome(something.lower()):
    print("Yes, it is a palindropme")
else:
    print("No, it is not a palindrome")
