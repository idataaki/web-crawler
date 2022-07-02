import requests

headers = {'Accept' : 'application/vnd.orcid+json'}

"0000-0003-2678-8281"

def orcid_user(orcid):
    res = requests.get("https://pub.orcid.org/v3.0/{}/person".format(orcid), headers=headers)
    js = res.json()
    fn = js['name']['given-names']['value']
    ln = js['name']['family-name']['value']
    id = js['name']['path']
    website = js['researcher-urls']['researcher-url'][0]['url']['value']
    email = js['emails']['email']
    return (fn, ln, orcid, website, email)

def orcid_works(orcid):
    lst = []
    res = requests.get("https://pub.orcid.org/v3.0/{}/works".format(orcid), headers=headers)
    group = res.json()['group']

    for g in group:
        t = g['work-summary'][0]['title']['title']['value']
        idt = g['work-summary'][0]['external-ids']['external-id'][0]['external-id-type']
        id = g['work-summary'][0]['external-ids']['external-id'][0]['external-id-value']
        jornal = g['work-summary'][0]['journal-title']['value']
        url = g['work-summary'][0]['url']['value']
        lst.append((t, jornal, url, idt, id))

    return lst

