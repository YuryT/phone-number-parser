import time
from requests import get
from typing import List

from .parsers.google_driven_parser import parse_by_phonenumbers
from .parsers.regex_driven_parser import  parse_by_regex

MODE_GOOGLE_DRIVEN = 1
MODE_REGEX = 2


class Company(object):
    name: str
    contact_pages: List[str]
    phone_numbers: List[str]

    def __init__(self, name, contact_pages):
        self.name = name
        self.contact_pages = contact_pages

    def get_contact_page_text(self, url):
        return get(url).text

    def refresh_contacts(self, mode):
        numbers_set = set()
        for contact_page in self.contact_pages:
            text = self.get_contact_page_text(contact_page)
            start_time = time.time()
            if mode == MODE_GOOGLE_DRIVEN:
                numbers_set.update(parse_by_phonenumbers(text))
            elif mode == MODE_REGEX:
                numbers_set.update(parse_by_regex(text))
            end_time = time.time()
            print(f'{contact_page} parsing time: {end_time - start_time}')
        self.phone_numbers = list(numbers_set)
