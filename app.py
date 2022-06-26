from bs4 import BeautifulSoup
from flask import Flask, render_template
from jinja2 import Template
import requests

URL = "https://scholar.google.com/citations?user=cIn8pGEAAAAJ&hl=en"

class user:
    def __init__(self, name, photo, description):
    #def __init__(self, name, photo, university, emails, phone, page, related, citations, h_index):
        self.name = name
        self.photo = photo
        self.description = description
        '''self.university = university
        self.emails = emails
        self.phone = phone
        self.page = page
        self.related = related
        self.citations = citations
        self.h_index = h_index'''

class paper:
    def __init__(self, title, author, link, cited, year):
        self.title = title
        self.author = author
        self.link = link
        self.cited = cited
        self.year = year


def get_url(url):
    req = requests.get(url)
    html = BeautifulSoup(req.text, 'html.parser')
    return html

#user
def get_user(html):
    
    name = html.find('title').get_text()
    name = name[0:name.index('-')]

    for meta in html.find_all('meta'):
        if(meta.get('property') == "og:image"):
            photo = meta.get('content')
        elif(meta.get('name') == "description"):
            description = meta.get('content')

    return user(name, photo, description)

#papers
def papers(html):
    papers_lst = []
    rows = html.find_all('tr')
    for r in rows:
        paper_name, authors, paper_link, cited, year = "", "", "", "", ""
        contents = r.find_all('td')
        if len(contents) == 0: continue
        for content in contents:
            c_class = content.get('class')[0]
            if c_class == 'gsc_a_t':
                paper_name = content.find('a').get_text()
                paper_link = "https://scholar.google.com" + content.find('a').get('href')
                authors = content.find('div').get_text()
            elif c_class == 'gsc_a_c':
                cited = content.find('a').get_text()
            elif c_class == 'gsc_a_y':
                year = content.find('span').get_text()
        if len(paper_name) > 0:
            papers_lst.append(paper(paper_name, authors, paper_link, cited, year))
    return papers_lst
    
def make_page():

    html = get_url("https://scholar.google.com/citations?user=cIn8pGEAAAAJ&hl=en")
    lst = papers(html)
    u = get_user(html)

    a = "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"
    b = "<title>Document</title><style>*,*::before,*::after {box-sizing: border-box;}"
    c = "body {background: #444;color: #fff;font-family: 'Poppins', sans-serif;margin: 0;}"
    d = "p{margin: 0 0 13px 0;}a {color: #fff;}.center {text-align: center;}"
    e = ".container {width: 95%;max-width: 1220px;margin: 0 auto;}.episode {display: grid;grid-template-columns: 0.3fr 3fr;position: relative;}"
    f = ".episode__number {font-size: 2vw;font-weight: 500;padding: 10px 0;position: sticky;top: 0;text-align: center;height: calc(5vw + 20px);transition: all 0.2s ease-in;}"
    g = ".episode__content { display: grid;grid-template-columns: 3fr 1fr;grid-gap: 10px;padding: 15px 15px;}"
    i = ".episode__content .title {font-weight: 300}.episode__content .story {line-height: 26px;}"
    j = "@media (max-width: 600px) {.episode__content {grid-template-columns: 1fr;}}@media (max-width: 576px) {.episode__content .story {font-size: 15px;}}</style></head><body>"
    l = "<div class=\"container\"><h1 class=\"left\">Papers</h1>{% for doc in documents %}"
    m = "<li><a href=\"{{ doc.link }}\">{{ doc.title }}</a></li><article class=\"episode\"><div class=\"episode__number\">{{doc.year}}</div><div class=\"episode__content\"><div class=\"title\">{{doc.author}}</div><div class=\"story\"><p>{{doc.cited}}</p></div></div></article>{% endfor %}</div></body></html>"
    o = "{% if user %}<div class=\"container\"><h1 class=\"center\">{{user.name}}</h1><article class=\"episode\"><img src=\"{{user.photo}}\" width=\"200\" height=\"259\"><div class=\"episode__content\"><div class=\"story\"><p>{{user.description}}</p></div></div></article></div>{% endif %}"

    html_string = a+b+c+d+e+f+g+i+j+o+l+m
    msg = Template(html_string).render(documents = lst, user = u)
    f = open('index.html', 'w')
    f.write(msg)

make_page()