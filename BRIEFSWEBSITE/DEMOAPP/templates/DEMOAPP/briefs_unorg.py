import requests
from bs4 import BeautifulSoup
import wikipedia
from collections import Counter
from PyDictionary import PyDictionary
import warnings
import emoji


dictionary = PyDictionary()

warnings.catch_warnings()
warnings.simplefilter("ignore")

features = "html.parser"

# Define the holders where we will place the top 3 terms when we find them
termOne = "Stephen King"
termTwo = "Lansdale, PA"
termThree = "chairman of the fed"


web_url = 'https://www.theatlantic.com/magazine/archive/2020/04/how-to-destroy-a-government/606793/'
# web_url = input('Enter article url: ')
#content_id = input('Enter content ID from HTML: ')

page = requests.get(web_url)
html_page = page.content
soup = BeautifulSoup(html_page, 'lxml')
#good_content = soup.find(id=content_id)
#good_content = soup.find('p', {'itemprop': 'articleBody'})
good_content = soup.find('body')
#body = soup.find('body').text
article_title = soup.title.string
#article_author = soup.find_all('c-byline__author')


# strip out all non-text content from site
just_the_text = (good_content.get_text())
# print(just_the_text)

# this is an attempt from https://stackoverflow.com/questions/6602111/how-to-search-for-a-capital-letter-within-a-string-and-return-the-list-of-words/41844782

# beginning of sentences is a problem I cant answer right now
# create empty list of my cap_words
cap_words = []
# strip all the other stuff off just_the_text
just_the_text = just_the_text.strip()
# identify all capitalized words over 3 chars and adds to cap_words
for word in just_the_text.split():
    if word.istitle() and len(word) > 3:
        cap_words.append(word)
    else:
        pass
# print(str("here is the first cap words: "))
# print(cap_words)
# must conv cap_words list into string
# from https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
data_set = ' '.join(map(str, cap_words))

# Then find the top 3 repeated words in that list
#data_set = cap_words

# split() returns list of all the words in the string
split_it = data_set.split()

# Pass the split_it list to instance of Counter class.
Counter = Counter(split_it)

# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = Counter.most_common(11)

print("")
print(str("Article Title: "))
print(str(article_title))
#print(str("Article Author: ") + str(article_author))
print("")
print(str("Here are the top 3 most frequent capitalized words from the article: "))
print(most_occur)

# How can I strip the frequency count, comma, and single ' off each index in list?
# maybe create a loop that grabs each item in list, grabs alphas, and places in new list?

# now assign top 3 to our variables
termOne, termTwo, termThree, termFour, termFive, = [most_occur[i] for i in (0, 1, 2, 3, 4)]
termSix, termSeven, termEight, termNine, termTen = [most_occur[i] for i in (5, 6, 7, 8, 9)]

print("")
print("Top 5 terms from the article and their definition:")
print("")

# This is the process to clean off all unwanted symbols from terms
# first term
#print(termOne)
# turn to string
termOne = str(termOne)
# define a funct that takes in string and reviews it replace all designated symbols with ""
def strip_chars(str, chars):
    return "".join(c for c in str if c not in chars)
# resulting is termOneDone which is stripped of symbols and nums and ready for wiki
termOneDone = (strip_chars(termOne, "(),'0123456789[]"))

# second term
#print(termTwo)
# turn to string
termTwo = str(termTwo)
# define a funct that takes in string and reviews it replace all designated symbols with ""
def strip_chars(str, chars):
    return "".join(c for c in str if c not in chars)
# resulting is termTwoDone which is stripped of symbols and nums and ready for wiki
termTwoDone = (strip_chars(termTwo, "(),'0123456789[]"))

# third term
#print(termThree)
# turn to string
termThree = str(termThree)
# define a funct that takes in string and reviews it replace all designated symbols with ""
def strip_chars(str, chars):
    return "".join(c for c in str if c not in chars)
# resulting is termThreeDone which is stripped of symbols and nums and ready for wiki
termThreeDone = (strip_chars(termThree, "(),'0123456789[]"))

# fourth term
# turn to string
termFour = str(termFour)
# define a funct that takes in string and reviews it replace all designated symbols with ""
def strip_chars(str, chars):
    return "".join(c for c in str if c not in chars)
# resulting is termThreeDone which is stripped of symbols and nums and ready for wiki
termFourDone = (strip_chars(termFour, "(),'0123456789[]"))

# fifth term
# turn to string
termFive = str(termFive)
# define a funct that takes in string and reviews it replace all designated symbols with ""
def strip_chars(str, chars):
    return "".join(c for c in str if c not in chars)
# resulting is termThreeDone which is stripped of symbols and nums and ready for wiki
termFiveDone = (strip_chars(termFive, "(),'0123456789[]"))


# Print first term
print(termOneDone)
try:
    print(wikipedia.summary(termOneDone, sentences=2))
except:
    try:
        print(dictionary.googlemeaning(termOneDone))
    except:
        print(emoji.emojize(':angry_face: Sorry, this term is too vague to define'))
print("")

# Print second term
print(termTwoDone)
try:
    print(wikipedia.summary(termTwoDone, sentences=2))
except:
    try:
        print(dictionary.meaning(termTwoDone))
        # print(dictionary.googlemeaning(termTwoDone))
    except:
        print(emoji.emojize(':angry_face: Sorry, this term is too vague to define'))
print("")

# Print third term
print(termThreeDone)
try:
    print(wikipedia.summary(termThreeDone, sentences=2))
except:
    try:
        print(dictionary.meaning(termThreeDone))
    except:
        print(emoji.emojize(':angry_face: Sorry, this term is too vague to define'))
print("")

# Print fourth term
print(termFourDone)
try:
    print(wikipedia.summary(termFourDone, sentences=2))
except:
    try:
        print(dictionary.meaning(termFourDone))
    except:
        print(emoji.emojize(':angry_face: Sorry, this term is too vague to define'))
print("")

# Print fifth term
print(termFiveDone)
try:
    print(wikipedia.summary(termFiveDone, sentences=2))
except:
    try:
        print(dictionary.meaning(termFiveDone))
    except:
        print(emoji.emojize(':angry_face: Sorry, this term is too vague to define'))
print("")


# https://www.theatlantic.com/business/archive/2020/05/fired-zoom-layoffs-coronavirus/611509/

# https://www.theatlantic.com/magazine/archive/2020/04/how-to-destroy-a-government/606793/


# main-content