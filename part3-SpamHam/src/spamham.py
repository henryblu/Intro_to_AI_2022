import os
import math

SMALL_NUMBER = 0.00001


def get_occurrences(filename):
    """ This function returns a dictionary of words and their occurrences from the sample ham and spam files.

    Each line of the input file must have the structure:
    'occurance word'
    eg: 
        1776 list

    The ouput dictionary will have the structure:
    key = word, value = occurance

    """
    results = {}
    dir_path = os.path.dirname(os.path.realpath(__file__))

    try:
        with open(os.path.join(dir_path, '..', filename)) as file:
            for line in file:
                count, word = line.strip().split(' ')
                results[word] = int(count)

        return results

    except FileNotFoundError:
        print("File %s was not found." % filename)
        raise
    except Exception as e:
        print("Something terrible happened: %s" % str(e))
        raise


def get_words(filename):
    """ This function returns a list of words from the inputed file.
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))

    try:
        with open(os.path.join(dir_path, '..', filename)) as file:
            words = [word for line in file for word in line.split()]

        return words

    except FileNotFoundError:
        print("File %s was not found." % filename)
        raise
    except Exception as e:
        print("Something terrible happened: %s", str(e))
        raise


class SpamHam:
    """ Naive Bayes spam filter
        :attr spam: dictionary of occurrences for spam messages {word: count}
        :attr ham: dictionary of occurrences for ham messages {word: count}
    """

    def __init__(self, spam_file, ham_file):
        self.spam = get_occurrences(spam_file)
        self.ham = get_occurrences(ham_file)

    def evaluate_from_file(self, filename):
        words = get_words(filename)
        return self.evaluate(words)

    def evaluate_from_input(self):
        words = input().split()
        return self.evaluate(words)

    def prob_ham(self, word):
        """ Probability that a word is in ham 
        """
        return self.ham.get(word, SMALL_NUMBER) / sum(self.ham.values())

    def prob_spam(self, word):
        """ Probability that a word is in spam 
        """
        return self.spam.get(word, SMALL_NUMBER) / sum(self.spam.values())

    def evaluate(self, words):
        """
        this function returns the probability that the inputed words are spam using the naive bayes algorithm and logerithms to avoid underflow errors.
        :param words: Array of str
        :return: probability that the message is spam (float)
        """

        logR = 0

        for word in words:
            prob_word_given_spam = self.prob_spam(word)
            prob_word_given_ham = self.prob_ham(word)
            logR += math.log(prob_word_given_spam) - math.log(prob_word_given_ham)
        
        R = math.exp(logR)
        return R / (1 + R)
