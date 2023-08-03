import spacy

nlp = spacy.load('en_core_web_sm')

word1 = nlp('cat')
word2 = nlp('monkey')
word3 = nlp('banana')
word4 = nlp('dog')

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print(word4.similarity(word1))
print(word4.similarity(word2))
print(word4.similarity(word3))

tokens = nlp('cat apple monkey banana dog')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I've lost my car in my car",
             "I'd like my boat back",
             "I will name my dog Diana"
             ]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


thing = input("say something")
#Using the advanced model I was able to observe the following:
#It's interestingly enough, able to regognise similarities between foods such as apples and
#bannas, and animals like monkey and cats. It's also able to see that
#there is a correlation between monkeys and bananas even if it is not as strong
#as the groups like animal+animal or fruit+fruit, adding in the example "dog"
#Made a very strong correlation with dog and cat, but less so than cat+monkey.
#Likewise, the fruits are very low much like cat with any other fruit

#Using the basic model I was able to observe the following:
#Scores in general are much higher, and the extreme affinity for cat and dog are lower.
#Instead fruits score much much higher for some reason now while the points for
#both being animals goes down.