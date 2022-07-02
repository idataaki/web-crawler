from linkedin_api import Linkedin

"ali-bohlooli-151915148"
class experience:
    def __init__(self, ti, co, start) -> None:
        self.ti = ti
        self.co = co
        self.start = start
class education:
    def __init__(self, deg, sch, field) -> None:
        self.deg = deg
        self.sch = sch
        self.field = field

def get_json(id):
    with open('userpass.txt', 'r') as f:
        lines = f.readlines()
    user = lines[0]
    passw = lines[1]
    api = Linkedin(user, passw)
    json = api.get_profile(id)
    contact_info_json = api.get_profile_contact_info(id)
    return json, contact_info_json

def linkedin_user(json, c_json):
    fn = json['firstName']
    ln = json['lastName']
    headline = json['headline']
    address = json['address']
    email = c_json['email_address']
    website = c_json['websites'][0]['url']
    phone = c_json['phone_numbers'][0]['number']
    return (fn, ln, headline, address, email, website, phone)

def linkedin_experience(json):
    lst =[]
    for exp in json['experience']:
        co = exp['companyName']
        ti = exp['title']
        start = exp['timePeriod']['startDate']['year']
        lst.append(experience(ti, co, start))
    return lst

def linkedin_skills(json):
    lst = []
    for skill in json['skills']:
        lst.append(skill['name'])
    return lst

def linkedin_education(json):
    lst = []
    for edu in json['education']:
        deg = edu['degreeName']
        sch = edu['schoolName']
        field = edu['fieldOfStudy']
        lst.append(education(deg, sch, field))
    return lst
