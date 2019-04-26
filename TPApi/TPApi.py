import hashlib
import random
from passgen import passgen
import requests


class BaseTPApi:
    def __init__(self):
        self.email = ""
        self.email_md5 = ""

    def api(self):
        return self

    def random(self, number: int = 8):
        return passgen(length=number, punctuation=False, digits=True, letters=True).lower()

    def domains(self):
        return self.fetch("domains/")

    def get_mail(self):
        return self.fetch("mail/id/" + self.email_md5 + "/")

    def get_one(self, id):
        return self.fetch("one_mail/id/" + id + "/")

    def get_source(self, id):
        return self.fetch("source/id/" + id + "/")

    def get_attachments(self, id):
        return self.fetch("attachments/id/" + id + "/")

    def delete(self, id):
        return self.fetch("delete/id/" + id + "/")

    def set_random_email(self, number: int = 8):
        url = random.choice(self.domains())
        name = self.random(number)
        self.email = name + url
        self.email_md5 = hashlib.md5(self.email.encode()).hexdigest()
        return self.email

    def set_email(self, email: str = None, name: str = None, url: str = None):
        if email:
            self.email = email
            self.email_md5 = hashlib.md5(self.email.encode()).hexdigest()
        elif name and url:
            self.email = name + url
            self.email_md5 = hashlib.md5(self.email.encode()).hexdigest()
        else:
            self.set_random_email()
        return self.email


class TPApi(BaseTPApi):
    def __init__(self):
        super().__init__()
        self.API_URL = "http://api2.temp-mail.org/request/"
        self.session = requests.Session()
        self.headers = {"Accept": "application/json"}

    def fetch(self, node):
        content = self.session.get(self.API_URL + node, headers=self.headers).json()
        return content
