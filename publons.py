import requests
"2c3dc7a0f65d7cf657d352099c3d8e2031301b8b"
headers = {
    'Authorization': 'Token 2c3dc7a0f65d7cf657d352099c3d8e2031301b8b',
    'Content-Type': 'application/json'}

url= "https://publons.com/api/v2/"
id = "ABG-4510-2021" #user must enter

def publons_user(id):
    r = requests.get("https://publons.com/api/v2/academic/{}/".format(id), headers=headers)
    js = r.json()
    name, publons_id, orcid, pubs_link, pubs_count = None, None, None, None, None

    try:
        name = js['publishing_name']
        publons_id = js['ids']['rid']
        orcid = js['ids']['orcid']
        pubs_link = js['ids']['url']
        pubs_count = js['publications']['count']
    except:
        print()
    return (name, publons_id, orcid, pubs_link, pubs_count)


def publons_publication(id):
    lst = []
    r = requests.get("https://publons.com/api/v2/academic/publication/?academic={}".format(id), headers=headers)
    #print(r.json())
    results = r.json()['results']
    next = r.json()['next']

    while next != None:
        rr = requests.get(next, headers=headers)
        results.extend(rr.json()['results'])
        next = rr.json()['next']

    for article in results:
        ti, date, puburl, doi, jornal, publisher = None, None, None, None, None, None

        try:
            ti = article['publication']['title']
            date = article['publication']['date_published']
            puburl = article['publication']['ids']['url']
            doi = article['publication']['ids']['doi']
            jornal = article['journal']['name']
            publisher = article['publisher']['name']
        except:
            print()
        lst.append((ti, date, puburl, doi, jornal, publisher))
    return lst
#publons_publication("2596772")