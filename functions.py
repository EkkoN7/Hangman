def char_in_word(word, list_append):    
    for word in word:
        for char in word:
            list_append.append(char.lower())