pc = "{%if doc.author != \"None\"%}<p>Author: {{doc.author}}</p>{%endif%}{%if doc.jornal != \"None\"%}<p>Jornal: {{doc.jornal}}</p>{%endif%}{%if doc.publisher != \"None\"%}<p>Publisher: {{doc.publisher}}</p>{%endif%}{%if doc.doi != \"None\"%}<p>DOI: {{doc.doi}}</p>{%endif%}{%if doc.year != \"None\"%}<p>Date: {{doc.year}}</p>{%endif%}{%if doc.gs_link != \"None\"%}<p><a href=\"{{doc.gs_link}}\">Google Scholar Link to paper</a></p>{%endif%}{%if doc.gs_cited != \"None\"%}<p><a href=\"\">citations in Google Scholar: {{doc.gs_cited}}</a></p>{%endif%}{%if doc.publons_url != \"None\"%}<p><a href=\"{{doc.publons_url}}\">Publons Link to paper</a></p>{%endif%}{%if doc.orcid_url != \"None\"%}<p><a href=\"{{doc.orcid_url}}\">ORCID Link to paper</a></p>{%endif%}"
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

m = "<li>{{ doc.title }}</li><article class=\"episode\"><div class=\"episode__number\">{{doc.index}}</div><div class=\"episode__content\"><div class=\"title\">"+ pc +"</div></div></article>{% endfor %}</div></body></html>"
o = "{% if user %}<div class=\"container\"><h1 class=\"center\">{{user.name}}</h1><article class=\"episode\"><img src=\"{{user.photo}}\" width=\"200\" height=\"259\"><div class=\"episode__content\"><div class=\"story\"><h3>{{user.headline}}</h3><p>Email: {{user.email}}</p><p>Website: {{user.website}}</p><p>Address: {{user.address}}  Phone: {{user.phone}}</p><p><a href=\"{{user.orcid}}\">ORCID</a>, <a href=\"{{user.publons_id}}\">Publons</a></p><p>this user has <a href=\"{{user.publon_publications_link}}\">{{user.publon_publications_count}} publications</a> on Publons</p></div></div></article></div>{% endif %}"
edu = "{% for edu in education %}<div class=\"container\"><h1 class=\"left\">Education</h1><li>{{edu.deg}}, {{edu.field}}</li><article class=\"episode\"><div class=\"episode__content\"><div class=\"story\"><p>School: {{edu.sch}}</p></div></div></article></div>{%endfor%}"
exp = "{% for exp in experience %}<div class=\"container\"><h1 class=\"left\">Experience</h1><li>{{exp.ti}}</li><article class=\"episode\"><div class=\"episode__content\"><div class=\"story\"><p>company: {{exp.co}}</p><p>start: {{exp.start}}</p></div></div></article></div>{%endfor%}"
skill = "{% for s in skills %}<div class=\"container\"><h1 class=\"left\">Skills</h1><li>{{s}}</li></div>{%endfor%}"

html_string = a+b+c+d+e+f+g+i+j+o+edu+exp+skill+l+m