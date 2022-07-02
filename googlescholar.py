from bs4 import BeautifulSoup
from jinja2 import Template
import requests

URL = "https://scholar.google.com/citations?user=cIn8pGEAAAAJ&hl=en&cstart=0&pagesize=1000"

class google_user:
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

class google_paper:
    def __init__(self, title, author, link, cited, year):
        self.title = title
        self.author = author
        self.link = link
        self.cited = cited
        self.year = year


def get_url(id):
    url = "https://scholar.google.com/citations?user={}&hl=en&cstart=0&pagesize=1000".format(id)
    req = requests.get(url)
    html = BeautifulSoup(req.text, 'html.parser')
    return html

def get_google_user(html):
    
    name = html.find('title').get_text()
    name = name[0:name.index('-')]

    for meta in html.find_all('meta'):
        if(meta.get('property') == "og:image"):
            photo = meta.get('content')
        elif(meta.get('name') == "description"):
            description = meta.get('content')

    return google_user(name, photo, description)

def google_papers(html):
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
            papers_lst.append(google_paper(paper_name, authors, paper_link, cited, year))
    return papers_lst
