def reverse_substrings(s):
    """Reverses each word in a string.
    !!! This is a placeholder function, replace it with your solution !!!
    """
    words = s.split(" ")
    reversed_words = []
    for word in words:
        reversed_word = ""
        for i in range(len(word) - 1, -1, -1):
            reversed_word += word[i]
        reversed_words.append(reversed_word)
    return reversed_words.join(" ")
