def count_words(text: str) -> dict:
    words = text.split()
    count_words = {}
    
    for i in words:
        count = words.count(i)
        if i not in count_words:
            count_words[i] = count
        
    

    return count_words

print(count_words("salom salom dunyo"))