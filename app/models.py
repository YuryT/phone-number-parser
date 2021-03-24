import time
import datetime
from requests import get, codes
from typing import List

from .parsers.google_driven_parser import parse_by_phonenumbers
from .parsers.regex_driven_parser import parse_by_regex

MODE_GOOGLE_DRIVEN = 1
MODE_REGEX = 2
MODE_REGEX_BS4 = 3

class ContactPage(object):
    url: str
    raw_html: str
    is_reload_required: bool
    is_parsed: bool

    def __init__(self, url):
        self.url = url
        self.is_reload_required = True
        self.is_parsed = False
        self.raw_html = ''

    def parse(self, mode):
        numbers_set = set()
        start_time = time.time()
        if self.is_reload_required:
            print(f'{self.url} wasn\'t loaded')
        if self.is_parsed:
            print(f'{self.url} already parsed')
        if mode == MODE_GOOGLE_DRIVEN:
            numbers_set = parse_by_phonenumbers(self.raw_html)
        elif mode == MODE_REGEX:
            numbers_set = parse_by_regex(self.raw_html)
        elif mode == MODE_REGEX_BS4:
            numbers_set.update(parse_by_regex(self.raw_html, bs4=True))
        end_time = time.time()
        print(f'{self.url} parsing time: {end_time - start_time}')
        return numbers_set


class Company(object):
    name: str
    contact_pages: List[ContactPage]
    phone_numbers: List[str]
    last_update_datetime: datetime.datetime

    def __init__(self, name, contact_pages_urls):
        self.name = name
        self.phone_numbers = []
        self.contact_pages = []
        for url in contact_pages_urls:
            self.contact_pages.append(ContactPage(url))

    def get_contact_page_text(self, page):
        response = get(page.url, timeout=5)
        if response.status_code == codes.ok:
            return response.text
        return None

    def load_contact_pages(self):
        # in real world - place for orm filter
        pages_to_load = [
            page for page in self.contact_pages if page.is_reload_required
        ]
        for page in pages_to_load:
            text = self.get_contact_page_text(page)
            if text:
                page.raw_html = text
                page.is_reload_required = False
                page.is_parsed = False
