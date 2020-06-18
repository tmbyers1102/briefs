import requests
from bs4 import BeautifulSoup
import wikipedia
from collections import Counter

# Define the holders where we will place the top 3 terms when we find them
termOne = "Stephen King"
termTwo = "Lansdale, PA"
termThree = "chairman of the fed"

page = requests.get('https://www.theatlantic.com/business/archive/2020/05/fired-zoom-layoffs-coronavirus/611509/')
soup = BeautifulSoup(page.content, 'html.parser')
good_content = soup.find(id='main-content')
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
most_occur = Counter.most_common(3)

print("")
print(str("Article Title: ") + str(article_title))
#print(str("Article Author: ") + str(article_author))
print("")
print(str("Here are the top 3 most frequent capitalized words from the article: "))
print(most_occur)

# How can I strip the frequency count, comma, and single ' off each index in list?
# maybe create a loop that grabs each item in list, grabs alphas, and places in new list?

# now assign top 3 to our variables
termOne, termTwo, termThree = [most_occur[i] for i in (0, 1, 2)]


"""
# this is an attempt to parse from https://www.geeksforgeeks.org/find-k-frequent-words-data-set-python/
# this uses the collections library to provide the top x number of repeated words
# for this attempt we have to switch just_the_text to data_set
data_set = just_the_text

# im adding the lower
data_set = data_set.lower()

# split() returns list of all the words in the string
split_it = data_set.split()

# Pass the split_it list to instance of Counter class.
Counter = Counter(split_it)

# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = Counter.most_common(3)

print(most_occur)

#now assign top 3 to our variables
termOne, termTwo, termThree = [most_occur[i] for i in (0, 1, 2)]
"""


"""
# This is an attempt to parse from https://www.javatpoint.com/program-to-find-the-duplicate-words-in-a-string
# for this effort change just_the_text to 'string'
string = just_the_text

# Converts the string into lowercase
string = string.lower()

# Split the string into words using built-in function
words = string.split(" ")

print("Duplicate words in a given string : ")
for i in range(0, len(words)):
    count = 1;
    for j in range(i + 1, len(words)):
        if (words[i] == (words[j])):
            count = count + 1
            # Set words[j] to 0 to avoid printing visited word
            words[j] = "0"

            # Displays the duplicate word if count is greater than 1
    if (count > 15 and words[i] != "0"):
        print(words[i])
"""


"""
# find the termOne
for x in just_the_text():
    # code that searches for repeated terms in list
    pass
    #assign that term
    x = termOne

# find termTwo
for x in just_the_text():
    # search again for repeated terms in list
    pass
    # make sure it is not termOne
    while x != termOne:
        x = termTwo

# find termThree
for x in just_the_text():
    # search again for repeated terms in list
    pass
    # make sure it is not termOne or termTwo
    while x != termOne | x != termTwo:
        x = termThree
"""

print("")
print("Top 3 terms from the article and their wiki definition:")
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


# Print first term as a title and provide 1st wiki sentence
print(termOneDone)
print(wikipedia.summary(termOneDone, sentences=2))
print("")

# Print second term as a title and provide 1st wiki sentence
print(termThreeDone)
print(wikipedia.summary(termThreeDone, sentences=2))
print("")

# Print third term as a title and provide 1st wiki sentence
print(termThreeDone)
print(wikipedia.summary(termThreeDone, sentences=2))
print("")


"""
text = []
for x in just_the_text:
    if isinstance(x, bs4.element.NavigableString):
        text.append(x.strip())
print(" ".join(text))
"""
# got the good content start and end narrowed down. Now need to parse out the crap and get only the article text
