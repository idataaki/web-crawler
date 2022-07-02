from bs4 import BeautifulSoup
from jinja2 import Template
import requests

import googlescholar, linkedin, orcid, publons

##name, photo, headline, email, website, address, phone, 
# orcid_id, publons_id, publon_publications_count, publon_publications_link
class User:
    def __init__(self, name, photo, headline, email, website, address, phone, 
    orcid_id, publons_id, publon_publications_count, publon_publications_link):
        self.name = name
        self.photo = photo
        self.headline = headline
        self.email = email
        self.website = website
        self.address = address
        self.phone = phone
        self.orcid_id = orcid_id
        self.publons_id = publons_id
        self.publons_publications_count = publon_publications_count
        self.publons_publications_link = publon_publications_link

#title, author, jornal, publisher, doi, year, gs_link, gs_cited, orcid_url, 
# publons_url,  external_id_type, external_id
class Paper:
    def __init__(self, title=None, author=None, jornal=None, publisher=None, doi=None, year=None, gs_link=None, gs_cited=None, orcid_url=None, publons_url=None,  external_id_type=None, external_id=None, index=None):
        self.title = str(title)
        self.author = str(author)
        self.jornal = str(jornal)
        self.publisher = str(publisher)
        self.doi = str(doi)
        self.year = str(year)
        self.gs_link = str(gs_link)
        self.gs_cited = str(gs_cited)
        self.orcid_url = str(orcid_url) 
        self.publons_url = str(publons_url)
        self.external_id_type = str(external_id_type)
        self.external_id = str(external_id)
        self.index = index

'''Google_Scholar_id = input('enter Google Scholar id:')
Linkedin_id = input('enter Linkedin id:')
Publons_id = input('enter Publons id:')
ORCID_id = input('enter ORCID id:')'''

# Google_Scholar_id = "cIn8pGEAAAAJ&hl"
# Linkedin_id = "ali-bohlooli-151915148"
# Publons_id = "ABG-4510-2021"
# ORCID_id = "0000-0003-2678-8281"

def update_paper(old_paper, new_paper):
    if old_paper.author.lower() != new_paper.author.lower() and new_paper.author != "None":
        if old_paper.author != "None":
            old_paper.author = old_paper.author + ", " + new_paper.author
        else:
            old_paper.author = new_paper.author

    if old_paper.jornal.lower() != new_paper.jornal.lower() and new_paper.jornal != "None":
        if old_paper.jornal != "None":
            old_paper.jornal = old_paper.jornal + ", " + new_paper.jornal
        else:
            old_paper.jornal = new_paper.jornal

    if old_paper.publisher.lower() != new_paper.publisher.lower() and new_paper.publisher != "None":
        if old_paper.publisher != "None":
            old_paper.publisher = old_paper.publisher + ", " + new_paper.publisher
        else:
            old_paper.publisher = new_paper.publisher

    if old_paper.doi.lower() != new_paper.doi.lower() and new_paper.doi != "None":
        if old_paper.doi != "None":
            old_paper.doi = old_paper.doi + ", " + new_paper.doi
        else:
            old_paper.doi = new_paper.doi

    if old_paper.orcid_url.lower() != new_paper.orcid_url.lower() and new_paper.orcid_url != "None":
        if old_paper.orcid_url != "None":
            old_paper.orcid_url = old_paper.orcid_url + ", " + new_paper.orcid_url
        else:
            old_paper.orcid_url = new_paper.orcid_url

    if old_paper.publons_url.lower() != new_paper.publons_url.lower() and new_paper.publons_url != "None":
        if old_paper.publons_url != "None":
            old_paper.publons_url = old_paper.publons_url + ", " + new_paper.publons_url
        else:
            old_paper.publons_url = new_paper.publons_url

    if old_paper.external_id_type.lower() != new_paper.external_id_type.lower() and new_paper.external_id_type != "None":
        if old_paper.external_id_type != "None":
            old_paper.external_id_type = old_paper.external_id_type + ", " + new_paper.external_id_type
        else:
            old_paper.external_id_type = new_paper.external_id_type

    if old_paper.external_id.lower() != new_paper.external_id.lower() and new_paper.external_id != "None":
        if old_paper.external_id != "None":
            old_paper.external_id = old_paper.external_id + ", " + new_paper.external_id
        else:
            old_paper.external_id = new_paper.external_id

def mix_user_data(gs_user, l_user, p_user, orcid_user):
    email, website = "", ""
    #publons -> name, publons_id, orcid, pubs_link, pubs_count
    publons_id, publon_publications_link, publon_publications_count = p_user[1], p_user[3], p_user[4]

    #linkedin -> fn, ln, headline, address, email, website, phone
    headline, address, email1, website1, phone = l_user[2], l_user[3], l_user[4], l_user[5], l_user[6]

    #gs -> name, photo, description
    name, photo, description = gs_user.name, gs_user.photo, gs_user.description

    #orcid -> fn, ln, id, website, email
    orcid_id, website2, email2= orcid_user[2], orcid_user[3], orcid_user[4]

    if email1 != None and email2 != None:
        if str(email1).lower() != str(email2).lower():
            email = email1
            for e in email2: email+=", "+e
        else:
            email = email1
    elif email1 == None and email2 != None:
        email = email2
    elif email2 == None and email1 != None:
        email = email1

    if website1 != None and website2 != None:
        if str(website1).lower() != str(website2).lower():
            website = website1 + ", " + website2
        else:
            website = website1
    elif website1 == None and website2 != None:
        website=website2
    elif website2 == None and website1 != None:
        website=website1

    return User(name, photo, headline, email, website, address, phone, orcid_id, publons_id, 
    publon_publications_count, publon_publications_link)

def mix_paper_data(gs_lst, orcid_works, p_publication):
    i, papers_indx = 0, {}
    all_papers = []

    #gs_lst -> title, author, link, cited, year
    for gs_paper in gs_lst:
        ind = papers_indx.get(str(gs_paper.title).lower())
        if ind == None:
            all_papers.append(Paper(title=gs_paper.title, author=gs_paper.author, gs_cited=gs_paper.cited, year=gs_paper.year, gs_link=gs_paper.link, index=i))
            papers_indx[str(gs_paper.title).lower()] = i
            i+=1
        else:
            #update the paper
            update_paper(all_papers[ind], Paper(title=gs_paper.title, author=gs_paper.author, year=gs_paper.year, gs_link=gs_paper.link))

    #orcid_works -> t, jornal, url, idt, id     
    for work in orcid_works:
        ind = papers_indx.get(str(work[0]).lower())
        if ind == None:
            all_papers.append(Paper(title = work[0], jornal = work[1], orcid_url=work[2], external_id_type=work[3], external_id=work[4], index=i))
            papers_indx[str(work[0]).lower()] = i
            i+=1
        else:
            #update the paper
            update_paper(all_papers[ind], Paper(jornal = work[1], orcid_url=work[2], external_id_type=work[3], external_id=work[4]))

    #p_publication -> ti, date, puburl, doi, jornal, publisher
    for pub in p_publication:
        ind = papers_indx.get(str(pub[0]).lower())
        if ind == None:
            all_papers.append(Paper(title = pub[0], year=pub[1], publons_url=pub[2], doi=pub[3], jornal=pub[4], publisher=pub[5], index=i))
            papers_indx[str(pub[0]).lower()] = i
            i+=1
        else:
            #update the paper
            update_paper(all_papers[ind], Paper(year=pub[1], publons_url=pub[2], doi=pub[3], jornal=pub[4], publisher=pub[5]))
    
    return all_papers

def html_to_string(file_address):
    result = ""
    with open(file_address, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line.replace("\n", '')
            result+=line
    return result

def make_page(Google_Scholar_id, ORCID_id, Linkedin_id, Publons_id):

    gs_html = googlescholar.get_url(Google_Scholar_id)
    gs_lst = googlescholar.google_papers(gs_html)
    gs_user = googlescholar.get_google_user(gs_html)

    orcid_user = orcid.orcid_user(ORCID_id)
    orcid_works = orcid.orcid_works(ORCID_id)

    l_json, l_c_json = linkedin.get_json(Linkedin_id)
    l_user = linkedin.linkedin_user(l_json, l_c_json)
    l_experience = linkedin.linkedin_experience(l_json)
    l_skills = linkedin.linkedin_skills(l_json)
    l_education = linkedin.linkedin_education(l_json)

    p_user = publons.publons_user(Publons_id)
    p_publication = publons.publons_publication(Publons_id)

    u = mix_user_data(gs_user, l_user, p_user, orcid_user)
    papers = mix_paper_data(gs_lst, orcid_works, p_publication)
    
    html_string = html_to_string('outputs/test.html')
    msg = Template(html_string).render(documents = papers, user = u, education=l_education, experience=l_experience, skills=l_skills)
    with open("outputs/index.html", "w", encoding="utf-8") as f:
        f.write(msg)

#make_page(Google_Scholar_id, ORCID_id, Linkedin_id, Publons_id)