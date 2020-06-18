from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  )
from .models import Post
import requests
from bs4 import BeautifulSoup
import wikipedia
from collections import Counter
from PyDictionary import PyDictionary
import warnings
import emoji


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'DEMOAPP/home.html', context)


def add(request):
    dictionary = PyDictionary()

    warnings.catch_warnings()
    warnings.simplefilter("ignore")

    features = "html.parser"

    weblink = request.GET['link']

    warnings.catch_warnings()
    warnings.simplefilter("ignore")

    features = "html.parser"

    web_url = weblink
    # web_url = input('Enter article url: ')
    # content_id = input('Enter content ID from HTML: ')

    page = requests.get(web_url)
    html_page = page.content
    soup = BeautifulSoup(html_page, 'lxml')
    good_content = soup.find('body')
    tit = soup.title.string

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

    termTwo = str(termTwo)
    # define a funct that takes in string and reviews it replace all designated symbols with ""
    def strip_chars(str, chars):
        return "".join(c for c in str if c not in chars)
    # resulting is termOneDone which is stripped of symbols and nums and ready for wiki
    term_two_done = (strip_chars(termTwo, "(),'0123456789[]"))

    termThree = str(termThree)
    # define a funct that takes in string and reviews it replace all designated symbols with ""
    def strip_chars(str, chars):
        return "".join(c for c in str if c not in chars)
    # resulting is termOneDone which is stripped of symbols and nums and ready for wiki
    term_three_done = (strip_chars(termThree, "(),'0123456789[]"))

    # Print first term
    try:
        term_one_defined = (wikipedia.summary(term_one_done, sentences=3))
    except:
        try:
            term_one_defined = (dictionary.googlemeaning(term_one_done))
        except:
            term_one_defined = (emoji.emojize(':angry_face: Sorry, this term is too vague to define'))

    # Print second term
    try:
        term_two_defined = (wikipedia.summary(term_two_done, sentences=3))
    except:
        try:
            term_two_defined = (dictionary.googlemeaning(term_two_done))
        except:
            term_two_defined = (emoji.emojize(':angry_face: Sorry, this term is too vague to define'))

    # Print third term
    try:
        term_three_defined = (wikipedia.summary(term_three_done, sentences=3))
    except:
        try:
            term_three_defined = (dictionary.googlemeaning(term_three_done))
        except:
            term_three_defined = (emoji.emojize(':angry_face: Sorry, this term is too vague to define'))

    #term_two_looking = True
    #while term_two_looking == True:


    return render(request, 'DEMOAPP/results.html', {
        'article_title': tit,
        'term_1': term_one_done,
        'term_1_def': term_one_defined,
        'term_2': term_two_done,
        'term_2_def': term_two_defined,
        'term_3': term_three_done,
        'term_3_def': term_three_defined,
        'url': weblink,
        }
    )


class PostListView(ListView):
    model = Post
    template_name = 'DEMOAPP/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'DEMOAPP/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


special_word = 'Special'

posts = [
    {
        'site_url': 'www.fakefake.com',
        'article_title': 'Fake Article Title',
        'date_posted': 'August 14, 2001',
        'word_1': 'Apple',
        'word_1_def': 'A fruit from a tree.',
        'word_2': 'Grape',
        'word_2_def': 'A fruit from a vine.',
        'word_3': 'Pear',
        'word_3_def': 'A weird fruit like a mishapped apple.'
    },
    {
        'site_url': 'www.bogus.com',
        'article_title': 'Bogus Article Title',
        'date_posted': 'May 14, 2091',
        'word_1': 'Pie',
        'word_1_def': 'A pastry from an oven.',
        'word_2': 'Sandwich',
        'word_2_def': 'A meal from a heaven.',
        'word_3': 'Pizza',
        'word_3_def': 'A food that makes you fat'
    }
]


def about(request):
    context = {
        'posts': posts
    }
    return render(request, 'DEMOAPP/about.html', context)

