import nltk
from nltk.corpus import reuters
from nltk.util import ngrams
import pandas as pd
import string
from nltk.probability import FreqDist

 

    
def get_ngram_frequency_distribution (n_value, tokens):

    ngrams_list = ngrams(tokens,n_value)
    ngrams_frequency_distribution = nltk.FreqDist(ngrams_list)
    print (ngrams_frequency_distribution)
    print(*ngrams_frequency_distribution.most_common(100), sep = "\n")
    return ngrams_frequency_distribution




if __name__ == "__main__":
   
  
    #print (len(reuters.words()))
    # Extract fileids from the reuters corpus
    fileids = reuters.fileids()

    # Initialize empty lists to store categories and raw text
    categories = []
    text_array = []

    text_string = ""

    # Loop through each file id and collect each files categories and raw text
    for file in fileids:
        categories.append(reuters.categories(file))
        text_array.append(reuters.raw(file))
        text_string += reuters.raw(file)

    # Combine lists into pandas dataframe. reutersDf is the final dataframe. 
    reutersDf = pd.DataFrame({'ids':fileids, 'categories':categories, 'text':text_array})

    #print(reutersDf)

    #tokenize the string that contains text of all files
    tweet = nltk.tokenize.TweetTokenizer()
    tokens = tweet.tokenize(text_string)
    #print (len(tokens), type(tokens))
    #print (tokens[:100])

    #create the list of lowercase tokens from the list of tokens above, such that
    #the former does not contain numbers and punctuation symbols
    tokens_filtered = []
    for i in range(len(tokens)):
        if not tokens[i].isdigit() and not tokens[i] in string.punctuation:
            tokens_filtered.append(tokens[i].lower()) 

    #print (len(tokens_filtered),'\n', tokens_filtered[:100])


    #create n_grams from the filtered token list
    bigram_fdist = get_ngram_frequency_distribution (2, tokens_filtered)
    trigram_fdist = get_ngram_frequency_distribution (3, tokens_filtered)
    fourgram_fdist = get_ngram_frequency_distribution (4, tokens_filtered)

    #get the list of possible ways to complete a strings of three words given the
    #filtered quadrigrams from the reuters database
    while True:
        input_string = input("Give me three words separated by single spaces to autocomplete: ")
        input_string = input_string.strip()
        print([ngram[3] for ngram in fourgram_fdist if ' '.join(ngram).lower().startswith(input_string.lower())], sep = "\n")

