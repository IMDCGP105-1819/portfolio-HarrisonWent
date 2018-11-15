most_Common_Words = []

word_Frequency = {
    "": 0
}

song = "I live in Tigerland I'm an indiana man " + \
    "I'm used to walk around with a snake in my hann " + \
    "Dr Bombay is my name and my father has the same " + \
    "But everything it changed here in Tigerland " + \
    "SOS the tiger took my father " + \
    "SOS the tiger took my brother " + \
    "SOS the tiger took my mother " + \
    "SOS the tiger took my family " + \
    "We lived outside Calcutta in a little wooden house " + \
    "I lived there with my family and 21 cows " + \
    "But now they all are gone and life is not so fun " \
    "But what can you expect here in Tigerland"

song = song.lower()

def match_word(word):
    if word in word_Frequency:
        word_Frequency[word] += 1
    else:
        word_Frequency[word] = 1


def analyse_song():

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    stripped_song = ""
    for char in song:
        if char not in punctuations:
            stripped_song = stripped_song + char

    words = stripped_song.split(" ")
    for word in words:
        match_word(word)


def common_word(minimum_Value):

    for word, value in word_Frequency.items():
        if value > minimum_Value:
            most_Common_Words.append({word: value})


analyse_song()

print("The most common word(s) is/are")
for word, value in word_Frequency.items():
    print("Word: ", "\"", word, "\"", "Frequency: ", value)

common_word(int(input("Please enter the least amount of times for a word: ")))

for word in most_Common_Words:
    print("Word: ", "\"", word)