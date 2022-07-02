import render

Google_Scholar_id = input('enter Google Scholar id:')
Linkedin_id = input('enter Linkedin id:')
Publons_id = input('enter Publons id:')
ORCID_id = input('enter ORCID id:')

render.make_page(Google_Scholar_id, ORCID_id, Linkedin_id, Publons_id)
print("Your File is Ready in index.html")

## ALi Bohlooli
# Google_Scholar_id = "cIn8pGEAAAAJ&hl"
# Linkedin_id = "ali-bohlooli-151915148"
# Publons_id = "ABG-4510-2021"
# ORCID_id = "0000-0003-2678-8281"

## M. R. Reshadinezhad
# enter Google Scholar id:UVoq7p0AAAAJ
# enter Linkedin id:mohammad-reza-reshadinezhad-28901553
# enter Publons id:2596772/mohammad-r-reshadinezhad
# enter ORCID id:0000-0003-4859-9879