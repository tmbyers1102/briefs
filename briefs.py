import requests
from bs4 import BeautifulSoup
import wikipedia
from collections import Counter
import warnings
import emoji

# Define the holders where we will place the top 3 terms when we find them
termOne = "Stephen King"
termTwo = "Lansdale, PA"
termThree = "chairman of the fed"


# just_the_text = ""

def main():
    """ function that asks user to copy and paste article link """
    request_link()
    """ function that takes in url from user, cleans it up, and prepares it to be analyzed"""
    get_the_content()
    """ function that reviews each word in article to see which is most popular/important
    and adds those words to a list"""
    analyze_content()
    """ function that assigns top terms as variables"""
    assign_variables()


def request_link():
    # Request article link from user
    web_url = input('Enter article url: ')
    return str(web_url)


def get_the_content():
    web_url = request_link()
    # activate Requests to bring in URL - define as 'page'
    page = requests.get(web_url)
    # activate .content function define as html_page
    html_page = page.content
    # activate BeautifulSoup to get html elements from URL - define as 'soup'
    soup = BeautifulSoup(html_page, 'lxml')
    # use the user provided content id and soup.find function to get needed text - define as 'good_content'
    good_content = soup.find('body')
    # grab the article title from BS using soup.title.string function - define as 'article_title'
    article_title = soup.title.string
    # strip all non-text characters from good_content - define as 'just_the_text'
    just_the_text = (good_content.get_text())
    # print(str(just_the_text))
    return just_the_text
    print("Article Title:")
    print(article_title)


def analyze_content():
    just_the_text = get_the_content()
    # create an empty list called 'cap_words'
    cap_words = []
    # use .strip function on 'just_the_text' to remove unwanted grammar stuff
    strip_text = just_the_text.strip()
    # create for loop that reviews each word in 'just the text' with the split function
    for word in strip_text.split():
        # if word is a title and longer than 3 ch add (append) to 'cap_words' list
        if word.istitle() and len(word) > 3:
            cap_words.append(word)
        # if word does not fit both criteria let it pass
        else:
            pass
    # conv 'cap_words' list to a string separated by a ' ' - define as 'data_set'
    data_set = ' '.join(map(str, cap_words))
    # use .split function to separate words in 'data_set' - define as 'split_it'(?)
    split_it = data_set.split()
    # use counter function to incorporate 'split_it' for counting
    counter = Counter(split_it)
    # use the .most_common function to produce list of the top x # of used terms and freq - define 'most_occur'
    most_occur = counter.most_common(4)
    #print(most_occur)
    return most_occur


def assign_variables():
    most_occur = analyze_content()
    termOne, termTwo, termThree, termFour = [most_occur[i] for i in (0, 1, 2, 3)]
    print("")
    print("Top 3 terms from the article and their wiki definition:")
    print("")
    print(termOne)

# print a blank line and then article title
# print blank line and then label 'here are the top 3...'
# print 'most_occur'
# assign top 3 indexes from 'most_occur' list to individual variables (termOne, termTwo, termThree)
# print label 'Here are those top 3 terms with their wiki...'

# define termOne as a str
# define a funct called strip_chars that reviews every ch in a str and returns to variable if not unwanted
# run 'strip_chars' function for termOne and define as new variable 'termOneDone'

# define termTwo as a str
# define a funct called strip_chars that reviews every ch in a str and returns to variable if not unwanted
# run 'strip_chars' function for termTwo and define as new variable 'termTwoDone'

# define termThree as a str
# define a funct called strip_chars that reviews every ch in a str and returns to variable if not unwanted
# run 'strip_chars' function for termThree and define as new variable 'termThreeDone'

# print final results
# print the stripped clean termOneDone
# use wikipedia.summary function to fetch the wiki blurb for termOneDone
# print the stripped clean termTwoDone
# use wikipedia.summary function to fetch the wiki blurb for termTwoDone
# print the stripped clean termThreeDone
# use wikipedia.summary function to fetch the wiki blurb for termThreeDone


if __name__ == '__main__':
    main()
