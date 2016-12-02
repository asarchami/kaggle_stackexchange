import nltk
from nltk.tokenize import sent_tokenize
from nltk import word_tokenize, pos_tag
import os


def _remove_duplicates(values):
    # Don't use this function unless you need it! this is a private function
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output
    # return value is a list of unique values


def process_content(sentence, stopwords):
    # this function creates tags from the sentence fiven to it
    # first argument is the sentence which we need to tagg and
    # and second one is the stopwords.
    # you probablty not gonna need to use this function in your code
    # TODO: may change the chunk parser for better chunking
    tokens = sent_tokenize(sentence, language='english')
    cp = nltk.RegexpParser(r"""chunk: {<NNP>*<NNPS>*<NN>*<NNS>*}""")
    chunks = []
    for sent in tokens:
        tree = cp.parse(pos_tag(word_tokenize(sent)))
        for subtree in tree.subtrees():
            if subtree.label() == 'chunk':
                chunks.append(subtree)
#     return chunks
    tags = []
    for tree in chunks:
        if len(tree.leaves()) == 1:
            if tree.leaves()[0][0] not in stopwords:
                tags.append(tree.leaves()[0][0])
        else:
            tags.append("-".join([t[0] for t in tree.leaves()]))
    tags
    return tags    # return value is a list of taggs


def create_taggs(data):
    # this function creates two two columns one with generated taggs and
    # the other with unique generated taggs and save them so we don't have to
    # do the process every time
    if os.path.exists('dataset/all_tagged.csv'):
        return pd.read_csv('dataset/all_tagged.csv', encoding='utf8')
    else:
        with open("kaggle/long_stopwords.txt") as f:
            stopwords = [word for line in f for word in line.split()]
        for i in range(len(data)):
            sentence = " ".join([data.loc[i, 'content'], data.loc[i, 'title']])
            data.loc[i, 'gen_tag'] = " ".join(
                process_content(sentence, stopwords))
            data.loc[i, 'gen_tag_unique'] = " ".join(
                _remove_duplicates(process_content(sentence, stopwords)))
        data.to_csv('dataset/all_tagged.csv', encoding='utf8')
        return data
    # returns the generated dataframe
