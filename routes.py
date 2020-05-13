import os
from flask import render_template, request
import nltk, re, pprint
from nltk import word_tokenize
from nltk.text import Text, ConcordanceIndex
from app import app

@app.route('/', methods=["GET", "POST"])
def index():
    books = {
        "book_1": "The Gruffalo",
        "book_2": "The BFG",
        "book_3": "The Little Prince",
        "book_4": "Where the Wild Things are"
    }
    query_word = None
    text = None
    book = None
    resource_path = None
    con = None
    join_sentences = []

    if request.method == "POST":
        book = request.form["book"]
        query_word = request.form["query_word"]

        if book == "The Gruffalo":
            resource_path = os.path.join(app.root_path, '/Users/hhdgk/Documents/Python/nltk/app/static/gruffalo.txt')
        elif book == "The BFG":
            resource_path = os.path.join(app.root_path, '/Users/hhdgk/Documents/Python/nltk/app/static/bfg.txt')
        elif book == "The Little Prince": 
            resource_path = os.path.join(app.root_path, '/Users/hhdgk/Documents/Python/nltk/app/static/tlp.txt')
        elif book == "Where the Wild Things are": 
            resource_path = os.path.join(app.root_path, '/Users/hhdgk/Documents/Python/nltk/app/static/wtwta.txt')
        
        if resource_path is not None:
            with open(resource_path, encoding="utf8") as resource:
                text = resource.read()
            text = nltk.Text(word_tokenize(text))
            for word in text[0]:
                con = text.concordance_list(query_word, width=40)
                sentence_list = []
                single_list = []
            for line in con:
                for x in line[0:3]:
                    if type(x) == list:
                        x = " ".join(x)
                    single_list.append(x)
                sentence_list.append(single_list)
                single_list = []
            
            for sentence in sentence_list:
                join_sentences.append(" ".join(sentence))
            join_sentences = set(join_sentences)
            join_sentences = list(join_sentences)
            
    
    return render_template("index.html", books=books, book=book, query_word=query_word, join_sentences=join_sentences)
    