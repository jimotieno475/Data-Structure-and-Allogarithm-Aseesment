import string

def word_frequency(sentence):
    # Remove punctuation and convert to lowercase
    sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()
    words = sentence.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

# Test the function
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
