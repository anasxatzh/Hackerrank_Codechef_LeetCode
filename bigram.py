# BIGRAM !!!!!

my_s = ['My name is', 'Anastasis chatzi effremidis']

bigrams = [b for l in my_s for b in zip(l.split(' ')[:-1], l.split(' ')[1:]) ]
print(bigrams)


# OR


##s = '    My name is Anastasis Minas Chatzi     '
##
##import nltk
##nltk_tokens = s.strip()
##nltk_tokens = nltk_tokens.split(' ')
##print(list(nltk.bigrams(nltk_tokens)))
