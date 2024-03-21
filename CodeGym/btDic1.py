def count_word_occurrences(text):
    num_words = {}
    text_list = text.split()
    
    for word in text_list:
        word = word.lower().strip()
        num_words[word] = num_words.get(word, 0) + 1
    
    return num_words

message = "This is a sample text. This text contains some sample words."
word_to_count = "sample"

word_occurrences = count_word_occurrences(message)
count = word_occurrences.get(word_to_count, 0)

print(f"The word '{word_to_count}' appears {count} times.")