class User(object):
    id = None
    first_name = None
    last_name = None
    gender = None
    dob = None
    email = None
    phone = None
    website = None
    address = None
    status = None

    def __init__(self, id=None, first_name=None, last_name=None, gender=None, dob=None, email=None, phone=None,
                 website=None, address=None, status=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.dob = dob
        self.email = email
        self.phone = phone
        self.website = website
        self.address = address
        self.status = status
