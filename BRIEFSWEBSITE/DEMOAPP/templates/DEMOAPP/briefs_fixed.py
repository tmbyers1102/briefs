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

web_url = 'https://www.theatlantic.com/magazine/archive/2020/04/how-to-destroy-a-government/606793/'
# web_url = input('Enter article url: ')
# content_id = input('Enter content ID from HTML: ')

page = requests.get(web_url)
html_page = page.content
soup = BeautifulSoup(html_page, 'lxml')
good_content = soup.find('body')
article_title = soup.title.string


# strip out all non-text content from site
just_the_text = (good_content.get_text())

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

data_set = ' '.join(map(str, cap_words))

# split() returns list of all the words in the string
split_it = data_set.split()

# Pass the split_it list to instance of Counter class.
sample = Counter(split_it)

# input values and their respective counts.
most_occur = sample.most_common(11)

# now assign to our variables
termOne, termTwo, termThree, termFour, termFive, = [most_occur[i] for i in (0, 1, 2, 3, 4)]

termOne = str(termOne)
# define a funct that takes in string and reviews it replace all designated symbols with ""
def strip_chars(str, chars):
    return "".join(c for c in str if c not in chars)
# resulting is termOneDone which is stripped of symbols and nums and ready for wiki
term_one_done = (strip_chars(termOne, "(),'0123456789[]"))

# Print first term
try:
    term_one_defined = (wikipedia.summary(term_one_done, sentences=2))
except:
    try:
        term_one_defined = (dictionary.googlemeaning(term_one_done))
    except:
        term_one_defined = (emoji.emojize(':angry_face: Sorry, this term is too vague to define'))

print(term_one_done)
print(term_one_defined)


