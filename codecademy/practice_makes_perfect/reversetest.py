def reverse(text):
    reversed_text = ""
    count = len(text)
    while count > 0:
        reversed_text += text[count - 1]
        count -= 1
    return reversed_text


print reverse("Python!")
