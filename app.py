import render

Google_Scholar_id = input('enter Google Scholar id:')
Linkedin_id = input('enter Linkedin id:')
Publons_id = input('enter Publons id:')
ORCID_id = input('enter ORCID id:')

render.make_page(Google_Scholar_id, ORCID_id, Linkedin_id, Publons_id)
print("Your File is Ready in index.html")