def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    chars = {}
    for i in text.lower():
        if i not in chars:
            chars[i] = 1
        else:
            chars[i] += 1
    return chars

def sort_on(dict):
    return dict["num"]

def order(chars):
    ch = []
    for k, v in chars.items():
        ch.append({"char": k, "num": v})
    ch.sort(reverse=True, key=sort_on)
    return ch
