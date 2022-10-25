# -*- coding: utf-8 -*-
"""
Introduction to AI
template for the NLP exercise
Teemu Roos, 05.10.2019
"""

import spacy
from spacy.symbols import nsubj, VERB

def nlp(input_file):
    nlp = spacy.load('en')

    # open the file and parse it using the English grammar ('en')
    source = open(input_file).read()
    doc = nlp(source)

    # iterate over the sentences in the document
    for sent in doc.sents:
        # check that the root of the sentence is a verb
        if sent.root.pos == VERB:

            # make note of the base form of the verb, e.g., "was"->"be"
            verb = sent.root.lemma_

            # iterate over words in the sentence
            for word in sent:

                # TODO
                # add code here to find the word 'Gregor' and check that it's 
                # dependency type (word.dep) is nsubj and that its parent 
                # (word.head) is the root node of the sentence
            
                if word.text == word.text and word.dep == word.dep and word.head == word.head:
                
                    # TODO
                    # add code here to increment the count of the verb verb
                    pass

    # print out the verbs that have count > 0 in the order of decreasing 
    # frequency, so that the most popular verb is printed first, etc.
    # the list should begin as follows:
    # say: 10
    # have: 7
    # be: 7
    return 0
