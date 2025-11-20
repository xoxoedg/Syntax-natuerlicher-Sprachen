import nltk
from nltk import word_tokenize

text = word_tokenize("And now for something completely different")
nltk.download('tagsets_json')

print(nltk.pos_tag(text))

nltk.help.upenn_tagset('RB')


from nltk.corpus import brown
text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
print(text.similar('big'))