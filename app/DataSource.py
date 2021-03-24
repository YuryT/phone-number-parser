from typing import List
from .models import Company


class DataSource:
    companies = List[Company]

    def __init__(self, companies=None):
        if companies:
            self.companies = companies
        else:
            self.companies = [Company(
                name='masterdel',
                contact_pages_urls=[
                    'https://masterdel.ru',
                    'https://masterdel.ru/reg.php',
                    'https://habr.com/ru/pos/' # 404 page
                ],
            ),
                Company(
                    name='repetitors.info',
                    contact_pages_urls=[
                        'https://repetitors.info/',
                        'https://repetitors.info/repetitor/',
                    ],
                )]

    # get data from db or api
    def get_companies_to_reload(self) -> List[Company]:
        # filter by Company.last_update_datetime should used here here
        return self.companies

    def get_companies_to_parse(self) -> List[Company]:
        # filter if company has unparsed contacts
        return self.companies

    def print_content(self):
        print('Output:')
        for company in self.companies:
            print(company.name)
            print(company.phone_numbers)
