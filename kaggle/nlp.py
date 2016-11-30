import nltk
from nltk.tokenize import sent_tokenize
from nltk import word_tokenize, pos_tag


def _remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output


def process_content(sentence):
    tokens = sent_tokenize(sentence, language='english')
    cp = nltk.RegexpParser(r"""chunk: {<NNP>*<NN>*}""")
    chunks = []
    for sent in tokens:
        tree = cp.parse(pos_tag(word_tokenize(sent)))
        for subtree in tree.subtrees():
            if subtree.label() == 'chunk':
                chunks.append(subtree)
    tags = []
    for tree in chunks:
        if len(tree.leaves()) == 1:
            if tree.leaves()[0][0] not in stopwords:
                tags.append(tree.leaves()[0][0])
        else:
            tags.append("-".join([t[0] for t in tree.leaves()]))
    tags
    return _remove_duplicates(tags)
