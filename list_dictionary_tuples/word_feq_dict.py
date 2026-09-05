def count_words(sentense):
    words = sentense.lower().split()
    freqency = {}
    for word in words:
        freqency[word] = freqency.get(word, 0) + 1
    print(freqency)
test = "The cat chased the rat and the rat ran away"
count_words(test)


students = {
    "Alice": {"Math": 85, "Science": 92, "English": 78},
    "Bob": {"Math": 70, "Science": 65, "English": 80},
    "Charlie": {"Math": 95, "Science": 98, "English": 91},
}