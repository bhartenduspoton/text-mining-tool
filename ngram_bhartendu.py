import nltk
from nltk.corpus import stopwords
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

## Here is collocation output
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()



def get_ngram(filename = None,_type=None,is_stopword=None):
    file_content = open(filename).read()
    # Get the tockens. Use word punctuations for tokenizing too other than spaces
    tokens = nltk.word_tokenize(file_content)
    text = nltk.Text(tokens)
    word_filter = lambda *w: word_to_find not in w
    ## Bigrams
    # ENABLE STOP WORDS
    #stopwords = stopwords.words('english')
    stopwords = []
    stopwords.append('.')
    #stopwords.append('The')
    stopwords.append(':')
    stopwords.append(',')
    stopwords.append(';')
    stopwords.append('`')
    stopwords.append('``')
    stopwords.append('\"')
    #print stopwords

    if is_stopword == 1:
        filtered_tokens = []
        for ftoken in tokens:
            ftoken_low = ftoken.lower()
            if ftoken not in stopwords:
                #print "Removing ######### " + ftoken
                filtered_tokens.append(ftoken)
    else:
         filtered_tokens = tokens


    if _type == 2:
        finder = BigramCollocationFinder.from_words(filtered_tokens,window_size=3)
    else:
        finder = TrigramCollocationFinder.from_words(filtered_tokens,window_size=3)
    # only bigrams that appear 3+ times
    finder.apply_freq_filter(1)
    lst = list(finder.ngram_fd.viewitems())
    #print lst
    ll = sorted(lst, key=lambda x: x[1])
    #ll = lst.sort(key=lambda x: x[0])
    #print ll
    res =[]
    for i in ll:
        k1 = []
        k  = list(i)
        k1.append(' '.join(k[0]))
        k1.append(k[1])
        res.append(k1)
        #raw_input()
        #print k1
    #print res
    return res


#get_ngram("fred-file.txt",2)
